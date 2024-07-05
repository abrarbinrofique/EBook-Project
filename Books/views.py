from django.shortcuts import render,redirect
from .forms import bookform

# Create your views here.
def AddBooks(request):
    if request.method=='POST':
        Bookform=bookform(request.POST,request.FILES)
        if Bookform.is_valid():
            Bookform.save()
            return redirect('home')
    else:
        Bookform=bookform()
    return render (request,'adminbook.html',{'form':Bookform})    



