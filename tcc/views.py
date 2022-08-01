from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .models import TCC
# Create your views here.

def home(request):
    return render(request, 'index.html')

def tcc(request,id):
    tcc_detail = get_object_or_404(TCC, id=id)
    return render(request, 'tcc.html', context={'tcc': tcc_detail})