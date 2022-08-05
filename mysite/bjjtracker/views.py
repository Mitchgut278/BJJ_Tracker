from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Position, Technique, Tag, MOTD
from .forms import TechniqueForm

import datetime
import random
# Create your views here.

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    techniques = Technique.objects.filter(
        Q(position__name__icontains=q)
    )

    positions = Position.objects.all()

    context = {'positions':positions, 'techniques':techniques}
    return render(request, 'bjjtracker/home.html', context)


def positionView(request, name):
    positions = Position.objects.all()
    position = Position.objects.get(name=name)
    techniques = Technique.objects.filter(position__name=position.name)
    context = {'positions':positions, 'position': position, 'techniques': techniques}
    return render(request, 'bjjtracker/position.html', context)


def techniqueView(request, pk):
    technique = Technique.objects.get(id=pk)
    context = {'technique': technique}
    return render(request, 'bjjtracker/technique.html', context)


def createTechnique(request):
    form = TechniqueForm()
    if request.method == 'POST':
        form = TechniqueForm(request.POST)
        form.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'bjjtracker/technique_form.html', context)


def updateTechnique(request, pk):
    technique = Technique.objects.get(id=pk)
    form = TechniqueForm(instance=technique)

    if request.method == 'POST':
        form = TechniqueForm(request.POST, instance=technique)
        if form.is_valid():
            form.save()
            return redirect('technique', pk=technique.id)
    context = {'technique':technique, 'form':form}
    return render(request, 'bjjtracker/technique_form.html', context)


def deleteTechnique(request, pk):
    technique = Technique.objects.get(id=pk)
    if request.method == 'POST':
        technique.delete()
        return redirect('home')
    context = {'obj':technique}
    return render(request, 'bjjtracker/delete.html', context)


def moveOfTheDay(request):
    date = datetime.date.today()
    try:
        motd = MOTD.objects.get(date=date)
        technique = Technique.objects.get(id=motd.technique.id)
    except Exception as e:
        technique = random.choice(list(Technique.objects.all()))
        motd = MOTD(
            date = date,
            technique = technique,
        )
        motd.save()
    if request.method == 'POST':
        if request.POST.get('completed'):
            motd.completed = True
            motd.save()
        if request.POST.get('skip'):
            technique = random.choice(list(Technique.objects.all()))
            motd.technique = technique
            motd.completed = False
            motd.save()
        
    context = {'technique' : technique, 'motd':motd}
    return render(request, 'bjjtracker/motd.html', context)