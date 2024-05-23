from apps.markets.models import Market

from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from django.conf import settings
from django.core.mail import send_mail
from django.db.models import Count, Case, When, Value
from django.db.models.functions import Coalesce

from apps.vendors.models import Vendor



@receiver(m2m_changed, sender=Market.vendors.through)
def send_email_m2m_add(sender, instance, action, pk_set, *args, **kwargs):
    if action == 'post_add':
        annotation = Market.objects.values('name').annotate(vendor_cnt=Count('vendors'))
        coalesce = Market.objects.aggregate(vendor_cnt=Coalesce(Count('vendors'), 0))
        when_case = Market.objects.values('name').annotate(mkt_type=Case(
            When(name=Value('test2'), then=Value('Wholesale')),
            When(name=Value('test1'), then=Value('Retail'))
            ))
        print('-------------------------ANNOTATIONS---------------------',annotation)
        print('-------------------------COALESCE---------------------',coalesce)
        print('-------------------------WHEN_CASE---------------------',when_case)
        # for i in pk_set:
        #     vendor = Vendors.objects.get(pk=i)
        #     print("----------------------NAME ADDED----------------", vendor.user.first_name)
        #     subject = f'Added {vendor.user.first_name} {vendor.user.last_name}'
        #     message = f'Hello {vendor.user.first_name},\n\nYou are added to the market!'
        #     from_email = settings.EMAIL_HOST_USER
        #     recipient_list = [vendor.user.email]
        #     send_mail(subject, message, from_email, recipient_list)


@receiver(m2m_changed, sender=Market.vendors.through)
def send_email_m2m_removed(sender, pk_set ,instance, action,*args, **kwargs):
    if action == 'post_remove': 
        for i in pk_set:
            vendor = Vendor.objects.get(pk=i)
            print("----------------------NAME REMOVED----------------", vendor.user.first_name)
            # subject = f'Removed {vendor.user.first_name} {vendor.user.last_name}'
            # message = f'Hello {vendor.user.first_name},\n\nYou are REmoved from the market!'
            # from_email = settings.EMAIL_HOST_USER
            # recipient_list = [i.user.email]
            # send_mail(subject, message, from_email, recipient_list)