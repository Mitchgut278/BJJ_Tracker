from django.shortcuts import render, redirect
from django.db.models import Q

from .helpers import getCurrentStreak
from .models import Position, Technique, Tag, MOTD
from .forms import TechniqueForm, CustomUserCreationForm

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

from django.shortcuts import get_object_or_404
import datetime
import random
# Create your views here.

def loginUser(request):
    page = 'login'
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
    context = {'page':page}
    return render(request, 'bjjtracker/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            user = authenticate(request, username=user.username, password=request.POST['password1'])
            
            if user is not None:
                login(request, user)
                return redirect('home')
                
    context = {'form': form, 'page':page}
    return render(request, 'bjjtracker/login_register.html', context)


@login_required(login_url='login')
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    techniques = Technique.objects.filter(
        Q(position__name__icontains=q)
    )

    positions = Position.objects.all()

    context = {'positions':positions, 'techniques':techniques}
    return render(request, 'bjjtracker/home.html', context)


@login_required(login_url='login')
def positionView(request, name):
    user = request.user
    positions = Position.objects.all()
    position = Position.objects.get(name=name)
    techniques = Technique.objects.filter(position__name=position.name, user=user)
    context = {'positions':positions, 'position': position, 'techniques': techniques}
    return render(request, 'bjjtracker/position.html', context)


@login_required(login_url='login')
def techniqueView(request, pk):
    technique = get_object_or_404(Technique, id=pk, user=request.user)
    context = {'technique': technique}
    return render(request, 'bjjtracker/technique.html', context)


@login_required(login_url='login')
def createTechnique(request):
    form = TechniqueForm()
    if request.method == 'POST':
        form = TechniqueForm(request.POST, request.FILES)
        technique = form.save(commit=False)
        technique.user = request.user
        technique.save()
        return redirect('home')
    context = {'form':form}
    return render(request, 'bjjtracker/technique_form.html', context)


@login_required(login_url='login')
def updateTechnique(request, pk):
    technique = Technique.objects.get(id=pk)
    form = TechniqueForm(instance=technique)

    if request.method == 'POST':
        form = TechniqueForm(request.POST, request.FILES, instance=technique)
        if form.is_valid():
            form.save()
            return redirect('technique', pk=technique.id)
    context = {'technique':technique, 'form':form}
    return render(request, 'bjjtracker/technique_form.html', context)


@login_required(login_url='login')
def deleteTechnique(request, pk):
    technique = Technique.objects.get(id=pk)
    if request.method == 'POST':
        technique.delete()
        return redirect('home')
    context = {'obj':technique}
    return render(request, 'bjjtracker/delete.html', context)


@login_required(login_url='login')
def moveOfTheDay(request):
    date = datetime.date.today()
    try:
        motd = MOTD.objects.get(date=date, user=request.user)
        technique = Technique.objects.get(id=motd.technique.id)
    except Exception as e:
        technique = random.choice(list(Technique.objects.filter(user=request.user)))
        motd = MOTD(
            date = date,
            technique = technique,
            user=request.user
        )
        motd.save()
    if request.method == 'POST':
        if request.POST.get('completed'):
            motd.completed = not motd.completed
            motd.save()
        if request.POST.get('skip'):
            technique = random.choice(list(Technique.objects.all()))
            motd.technique = technique
            motd.completed = False
            motd.save()
        
    context = {'technique' : technique, 'motd':motd}
    return render(request, 'bjjtracker/motd.html', context)


@login_required(login_url='login')
def moveOfTheDayHistory(request):
    user = request.user
    objects = MOTD.objects.filter(user=user).order_by('date')
    streak = getCurrentStreak(request)
    context = {'objects':objects, 'streak':streak}
    return render(request, 'bjjtracker/motd_history.html', context)