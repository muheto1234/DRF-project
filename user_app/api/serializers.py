from django.contrib.auth.models import User
from rest_framework import serializers
from user_app.models import Profile


class RegistraSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    image = serializers.ImageField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2', 'image']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        image = self.validated_data.get('image', None)

        if password != password2:
            raise serializers.ValidationError({'error': 'Les mots de passe ne correspondent pas'})

        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.ValidationError({'error': 'Cet email existe déjà'})

        if User.objects.filter(username=self.validated_data['username']).exists():
            raise serializers.ValidationError({'error': 'Ce nom d\'utilisateur existe déjà'})

        # Créer l'utilisateur en utilisant create_user pour gérer le mot de passe
        account = User.objects.create_user(
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            username=self.validated_data['username'],
            password=password  # set_password est géré par create_user
        )

        # Si une image est fournie, créer le profil avec l'image
        if image:
            profile = Profile(user=account, image=image)
            profile.save()
        else:
            Profile.objects.create(user=account)

        return account
    
    def update(self, instance, validated_data) :
        profile_data=validated_data('profile', None)
        instance.email=validated_data.get('email',instance.email)
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.username=validated_data.get('username',instance.username)
        instance.save()

        if profile_data :
            profile=Profile(user=instance)
            profile.image=profile_data.get('image',profile.image)

class UpdateUserSeriliazerOnly(serializers.ModelSerializer) :
    image=serializers.ImageField(source='profile.image', required=False)

    class Meta :
        model=User
        fields=("username","email","first_name","last_name","image")
    def update(self, instance, validated_data) :
        profile_data=validated_data.get('profile', {})
        instance.email=validated_data.get('email',instance.email)
        instance.first_name=validated_data.get('first_name',instance.first_name)
        instance.last_name=validated_data.get('last_name',instance.last_name)
        instance.username=validated_data.get('username',instance.username)
        instance.save()

        if profile_data :
            profile=Profile(user=instance)
            profile.image=profile_data.get('image',profile.image)

        return instance

class UpdateProfileSerializer(serializers.ModelSerializer):
    # Inclure les données du profil dans le sérialiseur utilisateur
    image = serializers.ImageField(source='profile.image', required=False)

    class Meta:
        model = User
        exclude = ("password", )  # Inclure tous les champs de User

    def update(self, instance, validated_data):
        # Récupérer les données du profil (s'il y en a)
        profile_data = validated_data.pop('profile', {})
        profile = instance.profile  # Accéder au profil de l'utilisateur

        # Traiter les champs Many-to-Many séparément
        groups = validated_data.pop('groups', None)
        user_permissions = validated_data.pop('user_permissions', None)

        # Mettre à jour les informations de l'utilisateur
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Mettre à jour les groupes (Many-to-Many)
        if groups is not None:
            instance.groups.set(groups)

        # Mettre à jour les permissions (Many-to-Many)
        if user_permissions is not None:
            instance.user_permissions.set(user_permissions)

        # Mettre à jour le profil s'il y a des données
        if profile_data:
            profile.image = profile_data.get('image', profile.image)
            profile.save()

        return instance

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Profile
        fields = ['user', 'image']

    def update(self, instance, validated_data):
        # Extraire les données utilisateur
        user_data = validated_data.pop('user', None)
        user = instance.user

        # Mettre à jour le profil
        instance.image = validated_data.get('image', instance.image)
        instance.save()

        # Mettre à jour l'utilisateur
        if user_data:
            user_serializer = UserSerializer(user, data=user_data, partial=True)
            if user_serializer.is_valid(raise_exception=True):
                user_serializer.save()

        return instance

class DeleteProfileSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Profile
        fields = "__all__"

class ListeUserSeriliazer(serializers.ModelSerializer):
    image = serializers.ImageField(source='profile.image', required=False, allow_null=True)

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "image")

    def to_representation(self, instance):
        # Créez un profil vide pour les utilisateurs sans profil (y compris les superutilisateurs)
        profile, created = Profile.objects.get_or_create(user=instance)

        # Continue avec la représentation de l'utilisateur et du profil
        representation = super().to_representation(instance)
        representation['image'] = profile.image.url if profile.image else None
        
        return representation
