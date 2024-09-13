from .serialization import (SiteSerializer,AttractionSerializerCreate,AttractionSerializer,ActiviteSerializer,
                            EquipementSerializer,EquipementSerializerCreate,ReviewSerializer,HoraireSerializer,
                            TarifSerializer,ReservationSerializer,LikeSerializer,ActiviteSerializerCreate,LikeSerializerCreate,
                            ReviewSerializerCreate,HoraireSerializerCreate,TarifSerializerCreate,ReservationSerializerCreate)

from tourisme_app.models import Site,Attraction,Activite,Equipement,Review,Horaire,Tarif,Reservation,Like
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .permission import IsadminUserOrReadyOnly,IsUserOrReadOnly
from rest_framework.permissions import IsAdminUser,IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import filters
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from tourisme_app.api.pagination import WatchListPagination
import logging
#views for Site
class CreateSite(generics.CreateAPIView) :
    serializer_class= SiteSerializer
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(chef_du_site=self.request.user)
    
class ListSite(generics.ListAPIView) :
    queryset=Site.objects.all()
    serializer_class=SiteSerializer
    permission_classes= [IsAuthenticated]

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['chef_du_site__username', 'chef_du_site__first_name' ,'chef_du_site__last_name' ,'nom_du_site','emplacement']
    search_fields = ['chef_du_site__username', 'chef_du_site__first_name' ,'chef_du_site__last_name' ,'nom_du_site','emplacement']
    pagination_class=WatchListPagination

class SiteAllReview(generics.ListAPIView) :
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer

    def get_queryset(self):
        pk=self.kwargs['pk']
        return Review.objects.filter(site=pk)
        
class AllReviewForSite(generics.ListAPIView) :
    serializer_class=ReviewSerializer
    permission_classes= [IsAuthenticated]

    def get_queryset(self):
        pk=self.kwargs['pk']
        try :
            return Review.objects.filter(site=pk)
        except Review.DoesNotExist :
            return Response({'error' : 'this site does not exist'},status=status.HTTP_404_NOT_FOUND)


class UpdateSite(generics.RetrieveUpdateAPIView) :
    queryset=Site.objects.all()
    serializer_class=SiteSerializer
    permission_classes= [IsUserOrReadOnly]

class DeleteSite(generics.RetrieveDestroyAPIView) :
    queryset=Site.objects.all()
    serializer_class=SiteSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailSite(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Site.objects.get(pk=pk)
            serializer=SiteSerializer(queryset)
            return Response(serializer.data)
        except Site.DoesNotExist :
            return Response({'error' : 'this site does not exist'},status=status.HTTP_404_NOT_FOUND)

#views for Attraction
class CreateAttraction(generics.CreateAPIView) :
    serializer_class= AttractionSerializerCreate
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        site=Site.objects.get(pk=pk)
        serializer.save(site=site)
    
class ListAttraction(generics.ListAPIView) :
    queryset=Attraction.objects.all()
    serializer_class=AttractionSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    search_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    pagination_class=WatchListPagination
   

class UpdateAttraction(generics.RetrieveUpdateAPIView) :
    queryset=Attraction.objects.all()
    serializer_class=AttractionSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteAttraction(generics.RetrieveDestroyAPIView) :
    queryset=Attraction.objects.all()
    serializer_class=AttractionSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailAttraction(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Attraction.objects.get(pk=pk)
            serializer=AttractionSerializer(queryset)
            return Response(serializer.data)
        except Attraction.DoesNotExist :
            return Response({'error' : 'this Atraction does not exist'},status=status.HTTP_404_NOT_FOUND)

#views for Activite

class CreateActivite(generics.CreateAPIView) :
    serializer_class= ActiviteSerializerCreate
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        site=Site.objects.get(pk=pk)
        serializer.save(site=site)
    
class ListActivite(generics.ListAPIView) :
    queryset=Activite.objects.all()
    serializer_class=ActiviteSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    pagination_class=WatchListPagination
   
    
    

class UpdateActivite(generics.RetrieveUpdateAPIView) :
    queryset=Activite.objects.all()
    serializer_class=ActiviteSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteActivite(generics.RetrieveDestroyAPIView) :
    queryset=Activite.objects.all()
    serializer_class=ActiviteSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailActivite(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Activite.objects.get(pk=pk)
            serializer=AttractionSerializer(queryset)
            return Response(serializer.data)
        except Activite.DoesNotExist :
            return Response({'error' : 'this Activite does not exist'},status=status.HTTP_404_NOT_FOUND)
        

#views for Equipement
class CreateEquipement(generics.CreateAPIView) :
    serializer_class= EquipementSerializerCreate
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        site=Site.objects.get(pk=pk)
        serializer.save(site=site)
    
class ListEquipement(generics.ListAPIView) :
    queryset=Equipement.objects.all()
    serializer_class=EquipementSerializerCreate
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    pagination_class=WatchListPagination
   

class UpdateEquipement(generics.RetrieveUpdateAPIView) :
    queryset=Equipement.objects.all()
    serializer_class=EquipementSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteEquipement(generics.RetrieveDestroyAPIView) :
    queryset=Equipement.objects.all()
    serializer_class=EquipementSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailEquipement(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Equipement.objects.get(pk=pk)
            serializer=EquipementSerializer(queryset)
            return Response(serializer.data)
        except Equipement.DoesNotExist :
            return Response({'error' : 'this Equipement does not exist'},status=status.HTTP_404_NOT_FOUND)

#views for Review
class CreateReview(generics.CreateAPIView) :
    serializer_class= ReviewSerializerCreate
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        site=Site.objects.get(pk=pk)
        user=self.request.user
        review_queryset=Review.objects.filter(site=site,user=user)
        if review_queryset.exists() :
            raise ValidationError('You have already reviewed this site!')
        if site.number_etoile==0 :
            site.avg_etoile=serializer.validated_data['etoile']
        else:
            site.avg_etoile=(site.avg_etoile + serializer.validated_data['etoile'])/2
            
        site.number_etoile =site.number_etoile + 1
        site.save()
        serializer.save(site=site,user=user)
    
class ListReview(generics.ListAPIView) :
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    pagination_class=WatchListPagination
   

class UpdateReview(generics.RetrieveUpdateAPIView) :
    queryset=Review.objects.all()
    serializer_class=ReviewSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteReview(generics.RetrieveDestroyAPIView) :
    queryset=Review.objects.all()
    serializer_class=ReviewSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailReview(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Review.objects.get(pk=pk)
            serializer=ReviewSerializer(queryset)
            return Response(serializer.data)
        except Review.DoesNotExist :
            return Response({'error' : 'this Review does not exist'},status=status.HTTP_404_NOT_FOUND)


#views for Horaire
class CreateHoraire(generics.CreateAPIView) :
    serializer_class= HoraireSerializerCreate
    permission_classes= [IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        user=self.request.user
        site=Site.objects.get(pk=pk)
        serializer.save(site=site,user=user)
    
class ListHoraire(generics.ListAPIView) :
    queryset=Horaire.objects.all()
    serializer_class=HoraireSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    pagination_class=WatchListPagination
   

class UpdateHoraire(generics.RetrieveUpdateAPIView) :
    queryset=Horaire.objects.all()
    serializer_class=HoraireSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteHoraire(generics.RetrieveDestroyAPIView) :
    queryset=Horaire.objects.all()
    serializer_class=HoraireSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailHoraire(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Horaire.objects.get(pk=pk)
            serializer=HoraireSerializer(queryset)
            return Response(serializer.data)
        except Horaire.DoesNotExist :
            return Response({'error' : 'this Review does not exist'},status=status.HTTP_404_NOT_FOUND)
        

#Views for Tarif
class CreateTarif(generics.CreateAPIView) :
    serializer_class=TarifSerializerCreate
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        site=Site.objects.get(pk=pk)
        serializer.save(site=site)

class ListTarif(generics.ListAPIView) :
    queryset=Tarif.objects.all()
    serializer_class=TarifSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement','title']
    pagination_class=WatchListPagination
   

class UpdateTarif(generics.RetrieveUpdateAPIView) :
    queryset=Tarif.objects.all()
    serializer_class=TarifSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteTarif(generics.RetrieveDestroyAPIView) :
    queryset=Tarif.objects.all()
    serializer_class=TarifSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailTarif(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Tarif.objects.get(pk=pk)
            serializer=TarifSerializer(queryset)
            return Response(serializer.data)
        except Tarif.DoesNotExist :
            return Response({'error' : 'this Tarif does not exist'},status=status.HTTP_404_NOT_FOUND)

#Views for Reservation
class CreateReservation(generics.CreateAPIView) :
    serializer_class=ReservationSerializerCreate
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        user=self.request.user
        site=Site.objects.get(pk=pk)
        serializer.save(site=site,user=user)

class ListReservation(generics.ListAPIView) :
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    pagination_class=WatchListPagination
   

class UpdateReservation(generics.RetrieveUpdateAPIView) :
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializerCreate
    permission_classes= [IsUserOrReadOnly]

class DeleteReservation(generics.RetrieveDestroyAPIView) :
    queryset=Reservation.objects.all()
    serializer_class=ReservationSerializer
    permission_classes= [IsUserOrReadOnly]

class DetailReservation(APIView) :
    def get(self,request,pk) :
        try :
            queryset=Reservation.objects.get(pk=pk)
            serializer=ReservationSerializer(queryset)
            return Response(serializer.data)
        except Reservation.DoesNotExist :
            return Response({'error' : 'this Reservation does not exist'},status=status.HTTP_404_NOT_FOUND)
        

#for Like
class CreateLike(generics.CreateAPIView) :
    serializer_class =LikeSerializerCreate
    permission_classes=[IsAuthenticated]

    def perform_create(self, serializer):
        pk=self.kwargs.get('pk')
        try:
            site = Site.objects.get(pk=pk)
        except Site.DoesNotExist:
            raise ValidationError("Site does not exist")
        user=self.request.user
        queryset_site=Like.objects.filter(site=site,user=user).first()

        if queryset_site :
            queryset_site.delete()
            site.number_like = site.number_like - 1
        else :
            site.number_like = site.number_like + 1
            serializer.save(site=site,user=user)
        site.save()
        

class LikeList(generics.ListAPIView):
    queryset=Like.objects.all()
    serializer_class=LikeSerializer
    permission_classes=[IsadminUserOrReadyOnly]

    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_fields = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    search_fields  = ['site__chef_du_site__username', 'site__chef_du_site__first_name' ,'site__chef_du_site__last_name' ,'site__nom_du_site','site__emplacement']
    pagination_class=WatchListPagination



