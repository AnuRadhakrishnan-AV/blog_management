import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    content = django_filters.CharFilter(lookup_expr='icontains')
    author = django_filters.CharFilter(field_name='author__username', lookup_expr='icontains')
    categories = django_filters.CharFilter(field_name='categories__name', lookup_expr='icontains')
    tags = django_filters.CharFilter(field_name='tags__name', lookup_expr='icontains')
    created_at = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['title', 'content', 'author', 'categories', 'tags', 'created_at']
