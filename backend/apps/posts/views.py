from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from backend.apps.posts.models import Posts
# Create your views here.


class IndexPage(ListView):
    template_name = 'index.html'
    queryset = Posts.objects.filter(is_active=True)
    context_object_name = 'post_list'
