<<<<<<< HEAD
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from . import forms
from .models import TCC, Autor, Curso, Orientador


>>>>>>> 60ffc6789874fbc16bf0d027fa3a8852ffa59f87

def home(request):
    return render(request, 'index.html')

@login_required
def tcc(request,id):
    tcc_detail = get_object_or_404(TCC, id=id)
    return render(request, 'tcc.html', context={'tcc': tcc_detail})

def criar(request, model):  
    form = eval(f'forms.{model.capitalize()}Form')
    if request.method == "POST":  
        form = form(request.POST)  
        if form.is_valid():  
            form.save() 
            model = form.instance
            return redirect('tcc:home')  
  
    else:  
        form = form()  
    return render(request,'criar_tcc.html',{'form':form, 'model': model.capitalize()})

def listar(request, model):
    if model.lower() == 'tcc':
        class_model = eval('TCC')
    else:
        class_model = eval(f'{model.capitalize()}')

    consultas = class_model.objects.all()
    return render(request, f'{model.lower()}.html', {'consultas':consultas})

