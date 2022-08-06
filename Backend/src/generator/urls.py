from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
<<<<<<< HEAD
    path('about/', views.about, name='about'),
    path('register', views.SignUp, name='register'),
    path('login', views.SignIn, name='login'),
    path('setting', views.AccountSetting.as_view(template_name ='AccountSettings.html'), name='setting'), 
    path('delete', views.DeleteAccount, name='delete'),
     
=======
     path('about/', views.about, name='about'),
        path('contact/', views.contact, name='contact'),
            path('privacyPolicy/', views.privacyPolicy, name='privacyPolicy'),
                    path('termsOfUse/', views.termsOfUse, name='termsOfUse'),




>>>>>>> 4c96fa57615a2474cf84bb219619441d957f3df9
]
