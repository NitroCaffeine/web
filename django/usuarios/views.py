from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.generic.edit import CreateView

from .forms import UserForm


# Create your views here.
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  
            messages.success(request, 'Your password was successfully updated!')
            return redirect('tcc:home')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'mudar_senha.html', {
        'form': form
    })

def listar(request):
    users = User.objects.all()
    return render(request, 'listar_users.html', context={'users': users})

def criar(request):
    if request.method == "POST": 
        form = UserForm(request.POST, request.FILES)  
        if form.is_valid():    
            form.save() 
            model = form.instance
            return redirect('tcc:home')  

    else:  
        form = UserForm()  
    return render(request,'criar.html',{'form':form})  


def atualizar(request, id):
    user = User.objects.get(id=id)
    form = UserForm(initial={'username': user.username,'last_name': user.last_name, 'email': user.email})
    if request.method == "POST":  
        form = UserForm(request.POST, instance=user)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('tcc:home')  
            except Exception as e: 
                pass    
    return render(request,'atualizar.html',{'form':form})

def deletar(request, id):
    user = User.objects.get(id=id)
    try:
        user.delete()
    except:
        pass
    return redirect('tcc:home')
