from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from . import forms
from .models import TCC, Autor, Curso, Orientador


def home(request):
    return render(request, 'index.html')

@login_required
def tcc(request,id):
    tcc_detail = get_object_or_404(TCC, id=id)
    return render(request, 'tcc.html', context={'tcc': tcc_detail})

def criar(request, model):
    form_model = eval(f'forms.{model.capitalize()}Form')
    if request.method == "POST": 
        form = form_model(request.POST, request.FILES)  
        if form.is_valid():    
            form.save() 
            model = form.instance
            return redirect('tcc:home')  

    else:  
        form = form_model()  
    return render(request,'criar.html',{'form':form, 'model': model.capitalize()})  

def listar(request, model):
    if model.lower() == 'tcc':
        class_model = eval('TCC')
    else:
        class_model = eval(f'{model.capitalize()}')

    consultas = class_model.objects.all()
    return render(request, f'{model.lower()}.html', {'consultas':consultas})

