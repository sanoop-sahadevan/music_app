
from .models import Music
from django.shortcuts import render
from .forms import MusicUploadForm
from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from django.contrib.auth import login

from django.contrib.auth.decorators import login_required

def indexView(request):
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Replace 'home' with the URL of your homepage
            return redirect('list')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



# from .forms import MusicForm

@login_required
def upload_music(request):
    if request.method == 'POST':
        form = MusicUploadForm(request.POST, request.FILES)
        if form.is_valid():
            music = form.save(commit=False)
            music.uploaded_by = request.user
            music.save()
            # return redirect('music_list')
    else:
        form = MusicUploadForm()
    
    return render(request, 'upload.html', {'form': form})














@login_required
def music_list(request):
    user = request.user
    private_music = Music.objects.filter(uploaded_by=request.user)
    public_music = Music.objects.filter(is_public=True).exclude(uploaded_by=user)
    context = {
        'private_music': private_music,
        'public_music': public_music,
    }
    return render(request, 'home.html', context)





from django.contrib.auth import logout


def logout_view(request):
    logout(request)
    return redirect('home')
