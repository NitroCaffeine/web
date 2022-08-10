from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import TCC, Autor
from . import forms
# Create your views here.

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


# def atualizar(request,model):
#     form = eval(f'forms.{model.capitalize()}Form')
#     if request.method == "POST":


 

