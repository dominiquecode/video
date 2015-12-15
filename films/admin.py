from django.contrib import admin
from .models import Film, Realisateur, Pays, Acteur, TypeFilm

# Register your models here.
admin.site.register(Film)
admin.site.register(Realisateur)
admin.site.register(Pays)
admin.site.register(Acteur)
admin.site.register(TypeFilm)

