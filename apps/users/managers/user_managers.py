from django.contrib.auth.models import BaseUserManager



class UserManager(BaseUserManager):
    def create_user(self, username, email, phone, password, **extra_fields):
        if phone is None:
            raise TypeError("Please enter Phone Number")
        if email is None:
            raise TypeError("Please enter email address")
        if username is None:
            raise TypeError("Please enter a username.")
        user = self.model(username=username, email=self.normalize_email(email), phone=phone, **extra_fields)
        user.set_password(password)
        user.save()
        return user
    
    def create_superuser(self, username, email, phone, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(username, email, phone, password, **extra_fields)
