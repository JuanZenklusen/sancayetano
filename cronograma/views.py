from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Cronograma, Musico, Misa, Capilla
from .forms import CronogramaForm, MusicoForm, MisaForm, CapillaForm
#from django.contrib import messages

def index(request):
    cronograma = Cronograma.objects.all().order_by('-date')
    context = {
        'cronograma' : cronograma,
    }
    return render(request, 'cronograma/index.html', context)




def view_crono(request, id):
    cronograma = Cronograma.objects.get(id=id)
    misa = Misa.objects.filter(cronograma_id=id).order_by('fecha')
    if request.method == 'GET':
        form = MisaForm(initial={'cronograma':id})
    if request.method == 'POST':
        form = MisaForm(request.POST)
        if form.is_valid():
            form.save()
    form = MisaForm(initial={'cronograma':id})
    context = {
        'cronograma' : cronograma,
        'misa' : misa,
        'form' : form,
    }
    return render(request, 'cronograma/view_crono.html', context)




def create_crono(request):
    if request.method == 'GET':
        form = CronogramaForm
        context = {
                'form': form,
            }
        return render(request, 'cronograma/create_crono.html', context)
    
    if request.method == "POST":
        form = CronogramaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('cronograma')
    
    
    
def delete(request, misa):
    delete_misa = Misa.objects.get(id=misa)
    delete_misa.delete()
    return redirect('cronograma')


def create_musico(request):
    if request.method == 'GET':
        form = MusicoForm
        context = {
            'form' : form
        }
        return render(request, 'cronograma/create_musico.html', context)
    
    
    if request.method == 'POST':
        form = MusicoForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect('cronograma')