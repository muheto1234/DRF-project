from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Site(models.Model) :
    chef_du_site=models.ForeignKey(User,on_delete=models.CASCADE)
    nom_du_site=models.CharField(max_length=100)
    avg_etoile=models.FloatField(default=0)
    number_etoile=models.IntegerField(default=0)
    number_like=models.IntegerField(default=0)
    emplacement=models.CharField(max_length=100)

    def __str__(self) :
        return self.nom_du_site
    
class Attraction(models.Model) :
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.title +"|"+ self.site.nom_du_site
    
class Activite(models.Model) :
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.title +"|"+ self.site.nom_du_site
    
class Equipement(models.Model) :
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    
    def __str__(self) :
        return self.title +"|"+ self.site.nom_du_site
    
class Review(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    etoile=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    commentaire=models.CharField(max_length=200)

    # def __str__(self) :
    #     return self.etoile +"|"+ self.site.nom_du_site

class Horaire(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    jour=models.DateField()
    heure_overture=models.TimeField()
    heure_fermeture=models.TimeField()
    nocturne=models.CharField(max_length=100)

class Tarif(models.Model) :
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    title=models.CharField(max_length=100)
    montant=models.PositiveIntegerField(blank=True,null=True)
    explication=models.CharField(max_length=100)

class Reservation(models.Model) :
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    nbre_adulte=models.PositiveIntegerField(blank=True,null=True)
    nbre_handicape=models.PositiveIntegerField(blank=True,null=True)
    nbre_enfant=models.PositiveIntegerField(blank=True,null=True)
    voyaje_journe=models.BooleanField(default=False)
    voyaje_nocturne=models.BooleanField(default=False)

class Like(models.Model) :
    site=models.ForeignKey(Site,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    

    class Meta:
        unique_together = ('site', 'user')



