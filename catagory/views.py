from catagory.forms import catagoryform
from django.views.generic import CreateView
from catagory.models import Catagory
from django.urls import reverse_lazy





class AddCatagory(CreateView):
    model = Catagory
    form_class=catagoryform
    template_name = "addcat.html"
    success_url=reverse_lazy('home')


