from django.shortcuts import render, redirect
from django.db.models import Q
from .models import Position, Technique, Tag
from .forms import TechniqueForm
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
