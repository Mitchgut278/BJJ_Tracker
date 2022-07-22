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


def createTechnique(request):
    form = TechniqueForm()
    context = {'form':form}
    return render(request, 'bjjtracker/technique_form.html', context)

