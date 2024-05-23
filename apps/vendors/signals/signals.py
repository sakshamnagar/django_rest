from apps.vendors.models import Vendor
from apps.users.models import User

from django.contrib.auth.models import Group
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.conf import settings
from django.core.mail import send_mail




@receiver(post_save, sender=Vendor)
def add_vendor_group(sender, created, instance, **kwargs):
    prefetch_related = User.objects.prefetch_related('vendor')
    print('----------------------PREFETCH RELATED-----------------',prefetch_related)
    # if created:
    #     instance.user.update(role__name = "Vendor")
        

# @receiver(post_save, sender=Vendors)
# def send_email(sender, created, instance, **kwargs):
#     if created:
#         subject = f'Welcome {instance.user.first_name} {instance.user.last_name}'
#         message = f'Hello {instance.user.first_name},\n\nWelcome! Account created!'
#         from_email = settings.EMAIL_HOST_USER
#         recipient_list = [instance.user.email]
#         send_mail(subject, message, from_email, recipient_list)



