from django.db import models
from django.utils.text import slugify

from base.models import BaseModel



class Category(BaseModel):
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100,default='slug')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Category,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.name