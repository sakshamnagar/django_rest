from base.models import BaseModel

from django.utils.text import slugify
from django.db import models

from apps.vendors.models import Vendor
from apps.categories.models import Category



class Product(BaseModel):
    vendor = models.ForeignKey(Vendor, related_name='product', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=100, default='slug')

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super(Product,self).save(*args,**kwargs)
        
    def __str__(self):
        return self.name