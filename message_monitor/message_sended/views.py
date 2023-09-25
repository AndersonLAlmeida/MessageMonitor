from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CustomAuthenticationForm, MessageSendedForm
from .models import CustomUser, MessageSended

# Home do Projeto
def home(request):
    return render(request,'home.html')

def sigup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:

            try:

                user = (CustomUser
                        .objects.create_user(username=request.POST['username'],
                                             password=request.POST['password1']))

                user.save()
                return redirect('dashboard')

            except:
                return render(request, 'sigup.html', {
                    'form': CustomUserCreationForm,
                    "error": 'Usuário já existe'

                })

        return render(request, 'sigup.html', {
            'form': CustomUserCreationForm,
            "error": 'senhas são diferentes'

        })
    else:
        form = CustomUserCreationForm()
    return render(request, 'sigup.html', {'form': form})

def sigin(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is None:
                return render(request, 'sigin.html', {
                    'form': form,
                    'error': 'Usuário ou senha está incorreto'
                })
            else:
                login(request, user)
                return redirect('monitor')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'sigin.html', {'form': form})

@login_required
def logout_system(request):
    logout(request)
    return redirect('home')
@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def add_message(request):
    if request.method == 'POST':
        message = MessageSendedForm(request.POST)
        message.save()
        return redirect('monitor')
    else:
        message = MessageSendedForm()
    return render(request, 'add_message.html', {'message': message})

@login_required
def monitor(request):
    table = MessageSended.objects.all()
    return render(request, 'monitor.html', {'table_rows': table})
