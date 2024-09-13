from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from tourisme_app.api.permission import IsadminUserOrReadyOnly,IsUserOrReadOnly
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from user_app.models import Profile
from .serializers import (UserSerializer,Profile,UpdateProfileSerializer,DeleteProfileSerializer,
                          RegistraSerializer,UpdateUserSeriliazerOnly,ProfileSerializer,ProfileSerializer)
# from rest_framework_simplejwt.tokens import RefreshToken
 
@api_view(['POST',])
def logout_review(request):
    if request.method=="POST":
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)

@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer=RegistraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        # if serializer.is_valid():
        #     account=serializer.save()
        #     data['response']="Registration Successful"
        #     data['username']= account.username
        #     data['email']=account.email
        #     refresh=RefreshToken.for_user(account)
        #     data['token'] = {
        #         'refresh':str(refresh),
        #         'access':str(refresh.access_token)
        #     }
        # else:
        #     data=serializer.errors
        # return Response(data)
    
#for user
class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsadminUserOrReadyOnly]

class UserDetail(APIView):
    permission_classes=[IsadminUserOrReadyOnly]
    def get(self,request,pk):
        try:
            queryset=User.objects.get(pk=pk)
            serializer=UserSerializer(queryset)
            return Response(serializer.data)
        except User.DoesNotExist :
            return Response({'error':'User Does Not Exist'},status=status.HTTP_404_NOT_FOUND)
        
class UserUpdate(generics.RetrieveUpdateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsadminUserOrReadyOnly]
        
class UpdateProfileView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateProfileSerializer
        
class UpdateUserOnlyView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UpdateUserSeriliazerOnly



class UserDestroy(generics.RetrieveDestroyAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer
    permission_classes=[IsadminUserOrReadyOnly]

    
class  RegistrationView(generics.CreateAPIView):
    serializer_class = RegistraSerializer


class ListUserProfil(generics.ListAPIView):
    queryset=User.objects.prefetch_related('profile').all()
    serializer_class=UpdateUserSeriliazerOnly

# class UpdateProfile(generics.RetrieveUpdateAPIView) :
    queryset=Profile.objects.all()
    serializer_class=ProfileSerializer
    permission_classes=[IsadminUserOrReadyOnly]

    def get_object(self):
        try:
            profile = self.request.user.profile
        except Profile.DoesNotExist:
            profile = Profile.objects.create(user=self.request.user)
        return profile

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)

class DetailsProfile(APIView):
    def get(self,request,pk) :
        try :
            queryset=User.objects.get(pk=pk)
            serializer=UpdateProfileSerializer(queryset)
            return Response(serializer.data)

        except Profile.DoesNotExist :
            return Response({'error':'User Does Not Exist'},status=status.HTTP_404_NOT_FOUND)
        
class DeleteProfil(generics.RetrieveDestroyAPIView) :
    queryset=Profile.objects.all()
    serializer_class =DeleteProfileSerializer

    def perform_destroy(self, instance):
        # Supprimer l'utilisateur lié au profil avant de supprimer le profil
        user = instance.user
        user.delete()
        # Supprimer le profil
        instance.delete()

