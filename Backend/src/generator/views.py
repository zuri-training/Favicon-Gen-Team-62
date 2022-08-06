from django.template import loader
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages, auth
from django.contrib.auth.models import User 
from .models import Profile, Favicons
from .form import UpdatePassword, EditProfileForm
from django.views.generic import UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def SignUp(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Exist")
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username Already Exist")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                
                # Log User in and redirect to setting page
                user_login = auth.authenticate(username=username, password=password)
                auth.login(request, user_login)

                # Create the profile page for the new user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(user=user_model, id_user=user_model.id)
                
                return redirect('home')    
        else:
            messages.info(request, "Password didn't match")
            return redirect('register')
    return render(request, 'register.html')

def SignIn(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:     
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "Invalid Login Details")
            return redirect('login')
    return render(request, 'login.html')

class AccountSetting(PasswordChangeView):
    form_class = UpdatePassword
    success_url = reverse_lazy('home')
    
def DeleteAccount(request):
    # user_model = get_object_or_404(User, id=id)
    user = User.objects.filter(username=request.user.username)
    if user.exists():
        user.delete()
        return redirect('login')
        
