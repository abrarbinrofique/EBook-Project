from django.urls import path,include
from .import views

urlpatterns = [
    path('depositMoney/',views.DepositMoneyView.as_view(),name='deposit'),
    path('buy/<int:id>',views.buybook,name='buy'),
    path('returnbook/<int:id>',views.bookreturn,name='returnbook'),
   

]
