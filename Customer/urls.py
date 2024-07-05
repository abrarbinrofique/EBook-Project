from django.urls import path,include
from .import views

urlpatterns = [
    path('registration/',views. Signup,name='signup'),
    path('login/',views.UserLogin.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.Userlogout.as_view(),name='logout'),
    
   
   

]
