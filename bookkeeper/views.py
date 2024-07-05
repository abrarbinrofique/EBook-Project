from django.shortcuts import render 
from catagory.models import Catagory
from Books.models import Book
from django.views.generic import DetailView
from Books.forms import Reviewform
from Books.models import Book


# def home(request):
#     book=Book.objects.all()
#     data=Catagory.objects.all()

#     return render(request,'home.html',{'book':book,'data':data}) 



def home(request,book_slug=None):

    cat=Catagory.objects.all()
    if book_slug is not None:
      bookcat=Catagory.objects.get(slug=book_slug)
      choosebook=Book.objects.filter(catagory=bookcat)
    #   print(choosecar)
    #   print(data)

    else:
        choosebook=Book.objects.all()
       
    return render(request,'home.html',{'data':cat,'book':choosebook})



class bookdescription(DetailView):
   model=Book
   pk_url_kwarg='id'
   form_class=Reviewform
   template_name='description.html'
   def post(self,request,*args, **kwargs):
        comment_form=Reviewform(data=request.POST)
        post=self.get_object()
        if comment_form.is_valid():
            new_comment=comment_form.save(commit=False)
            new_comment.Bookreview=post
            new_comment.save()
        return self.get(request,*args, **kwargs)
    

   def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            post=self.get_object()
            comments = post.comments.all()  # Assuming 'comments' is related_name in Review model
            comments_form = self.form_class() 
            context["comments"] =comments
            context["review_form"] =comments_form
            return context
        



    

   