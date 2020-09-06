import django_filters
from accounts.models import Comment,Doctor

class CFilter(django_filters.FilterSet):
    where = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['name','comment']


class DFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    address = django_filters.CharFilter(lookup_expr='icontains')
    choice = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Doctor
        fields = ['name','address','choice']
        #exclude = ['name','comment']