from django.contrib import admin

from .models import post


@admin.register(post)
class PostAdmin(admin.ModelAdmin):
    list_display =  ['id','title'] #coloca esto en el admin los campos
   