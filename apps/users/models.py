from django.db import models
from django.contrib.auth.models import AbstractUser, Permission

from base.models import BaseModel

from apps.users.managers.user_managers import UserManager



class Role(BaseModel):
    name = models.CharField(max_length=50)
    permissions = models.ManyToManyField(Permission)

    def __str__(self):
        return self.name
    

class User(AbstractUser):
    phone = models.CharField(max_length=30, unique=True)
    role = models.ForeignKey("users.Role", on_delete=models.CASCADE, null=True, blank=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)
    objects = UserManager()
    REQUIRED_FIELDS = ["email", "phone"]

    def __str__(self):
        return self.username


