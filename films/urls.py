from django.conf.urls import url
from films import views

urlpatterns = [
    url(r'^$', views.accueil, name='accueil'),
]
