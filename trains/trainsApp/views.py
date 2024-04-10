from django.http import HttpResponse
from django.http import HttpRequest
from django.shortcuts import render , redirect
from django.shortcuts import render, get_object_or_404
from .forms import TrainsForm
from .models import Trains
import random

def ajouter_train(request):
    if request.method == 'POST':
        form = TrainsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  
    else:
        form = TrainsForm()
    return render(request, 'trains/ajouter_train.html', {'form': form})


def index(request):
    listeTrains = Trains.objects.all()
    return render(request, 'trains/index.html', {'trains': listeTrains})



def train_detail(request, trainsid):
    train = Trains.objects.get(pk=trainsid)
    return render(request, "trains/detail.html", {"trains": train})

def recherche(request):
    query = request.GET.get('q')
    if query:
        resultats = Trains.objects.filter(destination__icontains=query)
    else:
        resultats = None
    return render(request, 'trains/recherche.html', {'resultats': resultats})

def random_train(request):
    random_train = Trains.objects.order_by('?').first()  
    return render(request, 'trains/random.html', {'random_train': random_train})





