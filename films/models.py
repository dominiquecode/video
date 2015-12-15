from django.db import models


# Create your models here.
# TODO: développer les modèles de l'application
class Personne(models.Model):
    date_naissance = models.DateField(blank=True, default='1900-01-01')
    date_deces = models.DateField(blank=True, default='1900-01-01')
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=20)

    class Meta:
        abstract = True


class Pays(models.Model):
    nom_pays = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = 'Pays'

    def __str__(self):
        return self.nom_pays


class Realisateur(Personne):
    nom_pays = models.ForeignKey(Pays)

    def __str__(self):
        return self.nom


class Acteur(Personne):
    nom_pays = models.ForeignKey(Pays)


    def __str__(self):
        return self.nom + ' ' + self.prenom


<<<<<<< Updated upstream
class Type_film(models.Model):
=======
class TypeFilm(models.Model):
>>>>>>> Stashed changes
    type = models.CharField(max_length=20, unique=True)
    commentaire = models.TextField()

    def __str__(self):
        return self.type


class Film(models.Model):
    titre = models.CharField(max_length=100)
    realisateur = models.ForeignKey(Realisateur)
    annee = models.IntegerField()
    nom_pays = models.ForeignKey(Pays)
<<<<<<< Updated upstream
    type_film = models.ForeignKey(Type_film)
=======
    type_film = models.ForeignKey(TypeFilm)
>>>>>>> Stashed changes
    acteurs = models.ManyToManyField(Acteur)
    choixStatus = [(None, 'Choisissez'),
                   ('ACHETE', 'Acheté'),
                   ('LOUE', 'Loué'),
                   ('PRETE', 'Prêté'),
                   ]
    status = models.CharField(choices=choixStatus, max_length=10)
    resume = models.TextField()
    choixAppreciation = [(None, 'Choisissez'),
                         ('EXCELLENT', 'Excellent'),
                         ('TRESBON', 'Trés bon'),
                         ('BON', 'Bon'),
                         ('MOYEN', 'Moyen'),
                         ('MEDIACRE', 'Médiacre'),
                         ('NAVET', 'Navet'),
                         ]
    appreciation = models.CharField(choices=choixAppreciation, max_length=10)
    photo = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.titre + " " + str(self.annee)