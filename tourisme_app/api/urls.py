from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from dj_rest_auth.views import (PasswordResetView, PasswordResetConfirmView, 
                                LoginView, LogoutView, PasswordChangeView)
from .views import(CreateSite,ListSite,UpdateSite,DeleteSite,DetailSite,CreateAttraction,
                   ListAttraction,UpdateAttraction,DeleteAttraction,DetailAttraction,CreateActivite,
                   ListActivite,UpdateActivite,DeleteActivite,DetailActivite,CreateEquipement,
                   ListEquipement,UpdateEquipement,DeleteEquipement,DetailEquipement,CreateReview,
                   ListReview,UpdateReview,DeleteReview,DetailReview,CreateHoraire,ListHoraire,
                   UpdateHoraire,DeleteHoraire,DetailHoraire,CreateTarif,ListTarif,UpdateTarif,
                   DeleteTarif,DetailTarif,CreateReservation,ListReservation,UpdateReservation,DeleteReservation,SiteAllReview,
                   DetailReservation,CreateLike,LikeList,AllReviewForSite)

urlpatterns = [
    #end point for site 
    path('CreateSite/',CreateSite.as_view(),name='create-site'),
    path('ListSite/',ListSite.as_view(),name='list-site'),
    path('<int:pk>/SiteAllReview',SiteAllReview.as_view(),name='list-site-all_review'),
    path('AllReviewForSite/<int:pk>/review',AllReviewForSite.as_view(),name='list-all_review-site'), #Pour voire tous les reviews d'un site
    path('UpdateSite/<int:pk>',UpdateSite.as_view(),name='update-site'),
    path('DeleteSite/<int:pk>',DeleteSite.as_view(),name='delete-site'),
    path('DetailSite/<int:pk>',DetailSite.as_view(),name='detail-site'),

    #end point for Attraction
    path('site/<int:pk>/CreateAttraction',CreateAttraction.as_view(),name='create-attraction'),
    path('ListAttraction/',ListAttraction.as_view(),name='list-Attraction'),
    path('UpdateAttraction/<int:pk>',UpdateAttraction.as_view(),name='update-Attraction'),
    path('DeleteAttraction/<int:pk>',DeleteAttraction.as_view(),name='delete-Attraction'),
    path('DetailAttraction/<int:pk>',DetailAttraction.as_view(),name='detail-Attraction'),

    #end point for Activite
    path('site/<int:pk>/CreateActivite/',CreateActivite.as_view(),name='create-Activite'),
    path('ListActivite/',ListActivite.as_view(),name='list-Activite'),
    path('UpdateActivite/<int:pk>',UpdateActivite.as_view(),name='update-Activite'),
    path('DeleteActivite/<int:pk>',DeleteActivite.as_view(),name='delete-Activite'),
    path('DetailActivite/<int:pk>',DetailActivite.as_view(),name='detail-Activite'),

    #end point for Equipement 
    path('site/<int:pk>/CreateEquipement/',CreateEquipement.as_view(),name='create-Equipement'),
    path('ListEquipement/',ListEquipement.as_view(),name='list-Activite'),
    path('UpdateEquipement/<int:pk>',UpdateEquipement.as_view(),name='update-Equipement'),
    path('DeleteEquipement/<int:pk>',DeleteEquipement.as_view(),name='delete-Equipement'),
    path('DetailEquipement/<int:pk>',DetailEquipement.as_view(),name='detail-Equipement'),

    #end point for Review
    path('site/<int:pk>/CreateReview/',CreateReview.as_view(),name='create-Review'),
    path('ListReview/',ListReview.as_view(),name='lisReview'),
    path('UpdateReview/<int:pk>',UpdateReview.as_view(),name='update-Review'),
    path('DeleteReview/<int:pk>',DeleteReview.as_view(),name='delete-Review'),
    path('DetailReview/<int:pk>',DetailReview.as_view(),name='detail-Review'),

    #end point for Horaire
    path('site/<int:pk>/CreateHoraire/',CreateHoraire.as_view(),name='create-Horaire'),
    path('ListHoraire/',ListHoraire.as_view(),name='list-Horaire'),
    path('UpdateHoraire/<int:pk>',UpdateHoraire.as_view(),name='update-Horaire'),
    path('DeleteHoraire/<int:pk>',DeleteHoraire.as_view(),name='delete-Horaire'),
    path('DetailHoraire/<int:pk>',DetailHoraire.as_view(),name='detail-Horaire'),

    #end point for Tarif
    path('site/<int:pk>/CreateTarif/',CreateTarif.as_view(),name='create-Tarif'),
    path('ListTarif/',ListTarif.as_view(),name='list-Horaire'),
    path('UpdateTarif/<int:pk>',UpdateTarif.as_view(),name='update-Tarif'),
    path('DeleteTarif/<int:pk>',DeleteTarif.as_view(),name='delete-Tarif'),
    path('DetailTarif/<int:pk>',DetailTarif.as_view(),name='detail-Tarif'),

    #end point for Reservation
    path('site/<int:pk>/CreateReservReservation/',CreateReservation.as_view(),name='create-Reservation'),
    path('ListReservation/',ListReservation.as_view(),name='list-Horaire'),
    path('UpdateReservation/<int:pk>',UpdateReservation.as_view(),name='update-Reservation'),
    path('DeleteReservation/<int:pk>',DeleteReservation.as_view(),name='delete-Reservation'),
    path('DetailReservation/<int:pk>',DetailReservation.as_view(),name='detail-Reservation'),

    #end point for Like
    path('site/<int:pk>/CreateLike/',CreateLike.as_view(),name='create-Like'),
    path('LikeList/',LikeList.as_view(),name='list-Like'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
