from django.contrib import admin
from .models import Film, Realisateur, Pays, Acteur, Type_film

# Register your models here.
admin.site.register(Film)
admin.site.register(Realisateur)
admin.site.register(Pays)
admin.site.register(Acteur)
admin.site.register(Type_film)

