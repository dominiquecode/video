from django.contrib import admin
<<<<<<< Updated upstream
from .models import Film, Realisateur, Pays, Acteur, Type_film
=======
from .models import Film, Realisateur, Pays, Acteur, TypeFilm
>>>>>>> Stashed changes

# Register your models here.
admin.site.register(Film)
admin.site.register(Realisateur)
admin.site.register(Pays)
admin.site.register(Acteur)
<<<<<<< Updated upstream
admin.site.register(Type_film)
=======
admin.site.register(TypeFilm)
>>>>>>> Stashed changes

