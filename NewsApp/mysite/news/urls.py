from django.urls import path, re_path
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Articles

urlpatterns = [
    path('', ListView.as_view(queryset=Articles.objects.all().order_by('-date')[:20],
         template_name="news/posts.html")),
    re_path(r'^(?P<pk>\d+)$', DetailView.as_view(model=Articles, template_name='news/post.html'))
]