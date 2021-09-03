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

def delete(request):
    #popup window asking for confirmation
    #if yes, proceed, if no, do nothing
    pass

def edit(request, hero_id):
    #render view w/ hero details populating a form
    #User can enter new values if they want
    #On submission, will grab existing superhero & update
    if request.method == "POST":
        existing_superhero = Superhero.objects.get(pk = hero_id)
        existing_superhero.name = request.POST.get('name')
        existing_superhero.alter_ego = request.POST.get('alter_ego')
        existing_superhero.primary_ability = request.POST.get('primary_ability')
        existing_superhero.secondary_ability = request.POST.get('secondary_ability')
        existing_superhero.catchphrase = request.POST.get('catchphrase')
        existing_superhero.save()
        return HttpResponseRedirect(reverse('superheroes:index'))
    else:
        current_hero = Superhero.objects.get(pk=hero_id)
        context = {
        'current_hero': current_hero
        }
        return render(request, 'superheroes/edit.html', context)