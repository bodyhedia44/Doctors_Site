import django_filters
from .models import Post


class BFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Post
        fields = ['title']
        exclude = ['time','image','content','author']