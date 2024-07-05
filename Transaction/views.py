from django.shortcuts import render,redirect
from Transaction.models import Transaction,wallet
from Transaction.forms import transactionform
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from django.contrib import messages
from Books.models import Book
from django.urls import reverse_lazy
# Create your views here.


class DepositMoneyView(LoginRequiredMixin,CreateView):
    form_class =transactionform
    template_name='deposit.html'
    success_url=reverse_lazy('profile')
 
    def form_valid(self, form):
        amount = form.cleaned_data.get('amount')

        user_wallet,created=wallet.objects.get_or_create(user=self.request.user)
        user_wallet.balance+=amount
        user_wallet.save()
        
     
        form.instance.user = self.request.user
        form.instance.amount = amount
        form.save()
        
        messages.success(
            self.request,
            f'{"{:,.2f}".format(float(amount))}$ was deposited to your account successfully'
        )

        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        user_wallet,created=wallet.objects.get_or_create(user=self.request.user)
        context['user_wallet']=user_wallet
        print(user_wallet.balance)
        return context

      
def buybook(request,id):
    user_wallet,created=wallet.objects.get_or_create(user=request.user)
    user_wallet.balance=0

    book=Book.objects.get(pk=id)
    print(book.price)
    if (book.price>request.user.account.balance):
        messages.success(request,'You Dont Have Enough Money in Your account,Add Money')
        return redirect('home')
    else:
         book.user.add(request.user)
         book.save()
         request.user.account.balance-=book.price
         request.user.account.save()
         return redirect('profile')


def bookreturn(request,id):
     book=Book.objects.get(pk=id)
     book.user.remove(request.user)
     book.save()
     request.user.account.balance+=book.price
     request.user.account.save()
     return redirect('profile')

