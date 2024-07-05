from catagory.models import Catagory
from django import forms

class catagoryform(forms.ModelForm):
    
    class Meta:
        model = Catagory
        fields = "__all__"

