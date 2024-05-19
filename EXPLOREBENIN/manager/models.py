from django.db import models
from manager.conf import * 
from manager.utils import *

# Create your models here.
class Departement(models.Model):
    intitule = models.CharField(max_length=MAX_LENGHT_INTITULE)

class Commune(models.Model):
    intitule = models.CharField(max_length=MAX_LENGHT_INTITULE)
    departement = models.ForeignKey(Departement, on_delete=models.CASCADE)
    
    def nom(self):
        return f"{self.departement.intitule} - {self.intitule}"

class Profil(models.Model):
    intitule = models.CharField(max_length=MAX_LENGHT_INTITULE)

class Utilisateur(models.Model):
    nom = models.CharField(max_length= MAX_LENGHT_NOM)
    prenom = models.CharField(max_length= MAX_LENGHT_PRENOM)
    date_naissance = models.DateField()
    sexe = models.BooleanField(default=True) # Par défaut, l'utilisateur est un homme.
    profil = models.ForeignKey(Profil, on_delete=models.CASCADE)
    
    email = models.EmailField(max_length=MAX_LENGHT_NOM, unique=True, null=True)
    password = models.CharField(max_length=MAX_LENGHT_NOM)
    photo = models.ImageField(upload_to="photos/Utilisateur", blank=True)
    
    def true_pass(self):
        return dechiffrement_cesar(self.password)
    
    def prenom_nom(self):
        return f"{self.prenom} {self.nom}"

class SiteTouristique(models.Model):
    nom = models.CharField(max_length=MAX_LENGHT_LIBELLE)
    description = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    
    def first_pic(self):
        return PhotoSite.objects.get(site=self, is_first=True)
    
    def other_pictures(self):
        return PhotoSite.objects.filter(site=self, is_first=False)
    
    def commentaires(self):
        return CommentaireSite.objects.filter(site=self)
    

class PhotoSite(models.Model):
    is_first = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/SiteTouristique", blank=True)
    site = models.ForeignKey(SiteTouristique, on_delete=models.CASCADE)

class Histoire(models.Model):
    libelle = models.CharField(max_length=MAX_LENGHT_LIBELLE)
    contenu = models.TextField()
    
    def first_pic(self):
        return PhotoHistoire.objects.get(histoire=self, is_first=True)
    
    def other_pictures(self):
        return PhotoHistoire.objects.filter(histoire=self, is_first=False)
    
    def commentaires(self):
        return CommentaireHistoire.objects.filter(histoire=self)

class PhotoHistoire(models.Model):
    is_first = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/Histoire", blank=True)
    histoire = models.ForeignKey(Histoire, on_delete=models.CASCADE)

class Evenement(models.Model):
    nom = models.CharField(max_length=MAX_LENGHT_LIBELLE)
    description = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    date_deroulement = models.DateField()
    date_fin = models.DateField(null=True)
    
    def first_pic(self):
        return PhotoEvenement.objects.get(event=self, is_first=True)
    
    def other_pictures(self):
        return PhotoEvenement.objects.filter(event=self, is_first=False)
    
    def date_deroulement_rep(self):
        return date_to_text(self.date_deroulement)
    
    def date_fin_rep(self):
        if self.date_fin:
            return date_to_text(self.date_fin)
        else:
            return ""
    
    def commentaires(self):
        return CommentaireEvent.objects.filter(event=self)

class PhotoEvenement(models.Model):
    is_first = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/Evenement", blank=True)
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)

class RessourceNaturelle(models.Model):
    nom = models.CharField(max_length=MAX_LENGHT_LIBELLE)
    description = models.TextField()
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE)
    
    def first_pic(self):
        return PhotoRessourceNaturelle.objects.get(ressource=self, is_first=True)
    def other_pictures(self):
        return PhotoRessourceNaturelle.objects.filter(ressource=self, is_first=False)
    
    def commentaires(self):
        return CommentaireRessource.objects.filter(ressource=self)

class PhotoRessourceNaturelle(models.Model):
    is_first = models.BooleanField(default=False)
    image = models.ImageField(upload_to="photos/RessourceNaturelle", blank=True)
    ressource = models.ForeignKey(RessourceNaturelle, on_delete=models.CASCADE)

class CommentaireSite(models.Model):
    site = models.ForeignKey(SiteTouristique, on_delete=models.CASCADE)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    
    def contenu_rep(self):
        c = self.contenu
        c = c.replace("\n", "°")
        return c
    
    def date_ajout_rep(self):
        return date_to_text(self.date_ajout)

class CommentaireHistoire(models.Model):
    histoire = models.ForeignKey(Histoire, on_delete=models.CASCADE)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    def date_ajout_rep(self):
        return date_to_text(self.date_ajout)
    def contenu_rep(self):
        c = self.contenu
        c = c.replace("\n", "°")
        return c

class CommentaireEvent(models.Model):
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    def date_ajout_rep(self):
        return date_to_text(self.date_ajout)
    def contenu_rep(self):
        c = self.contenu
        c = c.replace("\n", "°")
        return c

class CommentaireRessource(models.Model):
    ressource = models.ForeignKey(RessourceNaturelle, on_delete=models.CASCADE)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    contenu = models.TextField()
    date_ajout = models.DateTimeField(auto_now_add=True)
    def date_ajout_rep(self):
        return date_to_text(self.date_ajout)
    def contenu_rep(self):
        c = self.contenu
        c = c.replace("\n", "°")
        return c

class Circuit(models.Model):
    nom = models.CharField(max_length=MAX_LENGHT_LIBELLE)
    description = models.TextField()
    cout = models.IntegerField(default=0)
    
    is_special = models.BooleanField(default=False)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null=True)
    
    def description_rep(self):
        return truncatechars(self.description, 100)
    
    
    def longueur(self):
        return PointCircuit.objects.filter(circuit=self).count()
    
    def points(self):
        return PointCircuit.objects.filter(circuit=self).order_by('ordre')
    
    def hasnot_points(self):
        return PointCircuit.objects.filter(circuit=self).count() == 0
    
    def sites(self):
        return PointCircuit.objects.filter(circuit=self).values_list('site', flat=True).distinct()
    
    def ressources(self):
        return PointCircuit.objects.filter(circuit=self).values_list('res', flat=True).distinct()
    
    def events(self):
        return PointCircuit.objects.filter(circuit=self).values_list('event', flat=True).distinct()
    
    def last_ordre(self):
        lo = 0
        try:
            lo = PointCircuit.objects.filter(circuit=self).order_by('-ordre').first().ordre
        except:
            pass
        return lo

class PointCircuit(models.Model):
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    ordre = models.IntegerField()
    site = models.ForeignKey(SiteTouristique, on_delete=models.CASCADE, null=True)
    res = models.ForeignKey(RessourceNaturelle, on_delete=models.CASCADE, null=True)
    event = models.ForeignKey(Evenement, on_delete=models.CASCADE, null=True)

class Reservation(models.Model):
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    circuit = models.ForeignKey(Circuit, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100, blank=True)
    statut = models.BooleanField(default=False) # False = Validée, True = Effectuée
    montant_paye = models.PositiveIntegerField(default=0) # Montant payé en FCFA
    date_reservation = models.DateField(auto_now=True)