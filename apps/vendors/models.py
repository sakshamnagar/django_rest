from django.db import models
from django.utils.text import slugify

from base.models import BaseModel

from apps.users.models import User
  


class Vendor(BaseModel):
    user = models.OneToOneField(User, related_name="vendor", on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, default='slug')
    image = models.ImageField(upload_to='image', default='image/image.jpg')
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def save(self,*args,**kwargs):
        full_name = self.user.first_name + ' ' + self.user.last_name
        self.slug = slugify(full_name)
        super(Vendor,self).save(*args,**kwargs)

    
