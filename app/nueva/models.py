from django.db import models

# Create your models here.
class post(models.Model):
     title = models.CharField(max_length=275, verbose_name ='Título')
     content = models.CharField(max_length=100, verbose_name ='content')
     text = models.TextField( null = True, verbose_name ='text')
    
          
    
     def __str__(self):
        return self.title
