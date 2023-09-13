from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
  
def signup(request):
    if request.user.is_authenticated:
        return redirect('/home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            email= form.cleaned_data.get('email')
            user = authenticate(username=username, password=password, email=email)
            login(request, user)
            return redirect('/home')
        else:
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render(request, 'users/signup.html', {'form': form})
   
def home(request): 
    return render(request, 'users/home.html')
   
def signin(request):
    if request.user.is_authenticated:
        return render(request, 'users/home.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/home') #home
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'users/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
  
def home(request): 
    return render(request, 'users/home.html')
   
def signout(request):
    logout(request)
    return redirect('/')
