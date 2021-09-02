from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_nme = 'superheroes'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:hero_id>/', views.detail, name='detail')
]