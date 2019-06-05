from django.contrib import admin

# Register your models here.
from .models import product

class adminproduct(admin.ModelAdmin):
    list_display = ['pid','pname','pcost','pcolor']

admin.site.register(product,adminproduct)