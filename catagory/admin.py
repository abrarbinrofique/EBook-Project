from django.contrib import admin

# Register your models here.
from catagory.models import Catagory

# Register your models here.



class slugadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug']


admin.site.register(Catagory,slugadmin)