from django.urls import path,include
from .import views

urlpatterns = [
    path('addcatagory/',views.AddCatagory.as_view(),name='addcatagory'),
   

]
