from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


# Create your views here.

class IndexView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"


class PostView(DetailView):
    model = Post
    template_name = "post.html"
    context_object_name = "post"

    def get_object(self, queryset=None):
        return Post.objects.get(slug=self.kwargs["slug"])

