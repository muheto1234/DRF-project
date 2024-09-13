from django.contrib import admin
from .models import Site,Attraction,Activite,Equipement,Review,Horaire,Tarif,Reservation,Like

# Register your models here.

admin.site.register(Site)
admin.site.register(Attraction)
admin.site.register(Activite)
admin.site.register(Equipement)
admin.site.register(Review)
admin.site.register(Horaire)
admin.site.register(Tarif)
admin.site.register(Reservation)
admin.site.register(Like)
