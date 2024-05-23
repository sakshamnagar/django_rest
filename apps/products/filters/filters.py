import django_filters

from apps.products.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')
    vendor = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Product
        fields = ['name', 'vendor']