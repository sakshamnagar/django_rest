from django.db import models

from base.models import BaseModel

from apps.vendors.models import Vendor


class Market(BaseModel):
    name = models.CharField(max_length=50)
    vendors = models.ManyToManyField(Vendor, related_name='market')
    
    def __str__(self):
        return self.name