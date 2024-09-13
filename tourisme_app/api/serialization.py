from rest_framework import serializers
from tourisme_app.models import Site,Attraction,Activite,Equipement,Review,Horaire,Tarif,Reservation,Like
from django.contrib.auth.models import User


class SiteSerializer(serializers.ModelSerializer) :
    chef_du_site=serializers.StringRelatedField(read_only=True)
    class Meta :
        model= Site
        fields= "__all__"


class AttractionSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    class Meta :
        model= Attraction
        fields= "__all__"

class AttractionSerializerCreate(serializers.ModelSerializer) :
    class Meta :
        model= Attraction
        exclude=('site',)

class ActiviteSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    class Meta :
        model= Activite
        fields= "__all__"

class ActiviteSerializerCreate(serializers.ModelSerializer) :
    class Meta :
        model= Activite
        exclude=('site',)

class EquipementSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    class Meta :
        model= Equipement
        fields= "__all__"

class EquipementSerializerCreate(serializers.ModelSerializer) :
    class Meta :
        model= Equipement
        exclude=('site',)

class ReviewSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    user=serializers.CharField(source='user.username')
    class Meta :
        model= Review
        fields= "__all__"

class ReviewSerializerCreate(serializers.ModelSerializer) :
    user=serializers.StringRelatedField(read_only=True)
    class Meta :
        model= Review
        fields=['user','etoile','commentaire']

class HoraireSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    user=serializers.CharField(source='user.username')

    class Meta :
        model= Horaire
        fields= "__all__"

class HoraireSerializerCreate(serializers.ModelSerializer) :
    user=serializers.StringRelatedField(read_only=True)
    class Meta :
        model= Horaire
        exclude=('site',)

class TarifSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    class Meta :
        model= Tarif
        fields= "__all__"

class TarifSerializerCreate(serializers.ModelSerializer) :
    class Meta :
        model= Tarif
        exclude=('site',)

class ReservationSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    user=serializers.CharField(source='user.username')
    class Meta :
        model= Reservation
        fields= "__all__"

class ReservationSerializerCreate(serializers.ModelSerializer) :
    user=serializers.StringRelatedField(read_only=True)
    class Meta :
        model= Reservation
        exclude=('site',)

class LikeSerializer(serializers.ModelSerializer) :
    site=serializers.CharField(source='site.nom_du_site')
    user=serializers.CharField(source='user.username')
    class Meta :
        model= Like
        fields= "__all__"

class LikeSerializerCreate(serializers.ModelSerializer) :
    user=serializers.StringRelatedField(read_only=True)
    class Meta :
        model= Like
        exclude=('site',)


