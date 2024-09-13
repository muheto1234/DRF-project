from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, include

from .views import (registration_view,logout_review,UserList,UserDetail,UserUpdate,UserDestroy,UpdateProfileView,
                    RegistrationView,ListUserProfil,DetailsProfile,UpdateUserOnlyView,DeleteProfil)
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

urlpatterns = [
    # path('login/',obtain_auth_token,name='login'),
    path('register/',registration_view,name='register'),
    path('logout/',logout_review,name='logout'),
    path('api/token/',TokenObtainPairView.as_view(),name='token_obtain_pair'), #to login
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_reflesh'),

    #endpoint for User
    path('DetailsProfile/<int:pk>',DetailsProfile.as_view(),name='profile-detail'),
    path('UpdateProfileView/<int:pk>',UpdateProfileView.as_view(),name='profile-update'),
    path('UpdateUserOnlyView/<int:pk>',UpdateUserOnlyView.as_view(),name='user-only-update'),
    path('UserCreateProfile/',RegistrationView.as_view(),name='createprofile-user'),
    path('DeleteProfil/<int:pk>',DeleteProfil.as_view(),name='delete-user'),
    path('ListUserProfil/',ListUserProfil.as_view(),name='user-list'),

    
]