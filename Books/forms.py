from .models import Book,Review
from django import forms

from catagory.models import Catagory

class bookform(forms.ModelForm):
    catagory=forms.ModelMultipleChoiceField(widget = forms.CheckboxSelectMultiple,queryset =Catagory.objects.all())
    
    class Meta:
        model =Book 
        exclude=['user']



class Reviewform(forms.ModelForm):
    class Meta:
        model=Review
        fields=['name','email','text']

       