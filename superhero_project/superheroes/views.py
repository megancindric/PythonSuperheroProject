from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Superhero

# Create your views here.
def index(request):
    all_heroes = Superhero.objects.all()
    context = {
        'all_heroes': all_heroes
    }
    return render(request,'superheroes/index.html', context)

def detail(request, hero_id):
    single_hero = Superhero.objects.get(pk=hero_id)
    context = {
        'single_hero': single_hero
    }
    return render(request, 'superheroes/detail.html', context)

def create(request):
    if request.method == "POST":
        name = request.POST.get('name')
        alter_ego = request.POST.get('alter_ego')
        primary_ability = request.POST.get('primary_ability')
        secondary_ability = request.POST.get('secondary_ability')
        catchphrase = request.POST.get('catchphrase')
        my_hero = Superhero(name=name, alter_ego=alter_ego, primary_ability=primary_ability, secondary_ability=secondary_ability, catchphrase=catchphrase)
        my_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        return render(request, 'superheroes/create.html')

def delete(request, hero_id):
    current_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        current_hero.delete()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
        'current_hero': current_hero
        }
        return render(request, 'superheroes/delete.html', context)

def edit(request, hero_id):
    current_hero = Superhero.objects.get(pk=hero_id)
    if request.method == "POST":
        current_hero.name = request.POST.get('name')
        current_hero.alter_ego = request.POST.get('alter_ego')
        current_hero.primary_ability = request.POST.get('primary_ability')
        current_hero.secondary_ability = request.POST.get('secondary_ability')
        current_hero.catchphrase = request.POST.get('catchphrase')
        current_hero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        context = {
        'current_hero': current_hero
        }
        return render(request, 'superheroes/edit.html', context)