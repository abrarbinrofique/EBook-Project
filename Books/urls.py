from django.urls import path,include
from .import views

urlpatterns = [
    path('addbook/',views.AddBooks,name='addbook'),
 
  
    

]
