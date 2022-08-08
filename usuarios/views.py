from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import redirect, render


# Create your views here.
def alterar_senha(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('tcc:home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'alterar_senha.html', {'form_senha': form_senha})
