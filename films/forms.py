from django import forms
from .models import Film

class FilmForm(forms.Form):
    titre = forms.CharField(max_length=100, required=False)
    realisateur = forms.CharField(max_length=40, required=False)
    annee = forms.IntegerField(None, required=False)
    choixStatus = (('ACHETE', 'Acheté'),
                   ('LOUE', 'Loué'),
                   ('PRETE', 'Prêté'),)
    status = forms.ChoiceField(choices=choixStatus, required=False)
    resume = forms.CharField(None, widget=forms.Textarea)
    choixAppreciation = (('EXCELLENT', 'Excellent'),
                         ('TRESBON', 'Trés bon'),
                         ('BON', 'Bon'),
                         ('MOYEN', 'Moyen'),
                         ('MEDIACRE', 'Médiacre'),
                         ('NAVET', 'Navet'),)
    appreciation = forms.ChoiceField(choices=choixAppreciation, required=False)


class FilmModelForm(forms.ModelForm):
    class Meta:
        model = Film
        fields = ['titre', 'realisateur', 'annee', 'nom_pays', 'type_film',
                  'acteurs', 'status', 'appreciation', 'resume', 'photo']
