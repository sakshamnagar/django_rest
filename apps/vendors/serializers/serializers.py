from rest_framework import serializers

from apps.vendors.models import Vendor
from apps.users.models import User



class VendorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vendor
        fields = ('user', 'id', 'image',)


class VendorCreateSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True, required = False)

    class Meta:
        model = Vendor
        fields = ('user', 'id', 'image',)


        