from django.shortcuts import render
from .forms import FilmForm, FilmModelForm


# Create your views here.
def accueil(request):
    form = FilmModelForm()
    return render(request, 'accueil.html', {'filmform': form})



def index(request):
    return render(request, 'index.html', {})
