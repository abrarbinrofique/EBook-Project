from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login,logout
from django.views.generic import CreateView,FormView
from Customer.forms import userregistrationform 
from django.urls import reverse_lazy
from django.contrib import messages
from Books.models import Book
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.



def Signup(request):
     if request.method=='POST':
        form=userregistrationform (request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'you successfully add your account,now login here!')
            return redirect('login')
        
    
     else:
        form=userregistrationform ()
     return render (request,'signup.html',{'form':form})

    #     form
    #     return super().form_valid(form)
    


class UserLogin(LoginView):
    template_name='login.html'
    def get(self, request: HttpRequest):
        return super().get(request)
    

    def form_valid(self, form):
        username=form.cleaned_data.get('username')
        
        return super().form_valid(form)
    

    def form_invalid(self, form):
        messages.success(self.request,'Logged in information incorrect')
        return super().form_invalid(form)
    

    def get_context_data(self, **kwargs) :
        context=super().get_context_data(**kwargs)
        context['type']='Login'
        return context
    
    def get_success_url(self):
        messages.success(self.request,f'welcome to to your profile {self.request.user.first_name}')
        return reverse_lazy('profile')
    


def profile(request):
  if request.user.is_authenticated:
    profilebook=Book.objects.filter(user=request.user)
    print(profilebook)
    return render(request,'profile.html',{'profilebook':profilebook})
  else:
      return redirect('profile')






class Userlogout(LogoutView):
    # logout(request)
    def get_success_url(self):
      messages.success(self.request,'Logout Successfully')
      return reverse_lazy('login')
    