from django.shortcuts import render, resolve_url
from django.views.generic import ListView, DetailView, FormView
from blog.models import Post, Category, Comment
from django.forms import formset_factory
from blog.forms import CommentForm, commentform_factory


# Create your views here.
def index(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    return render(request, "bueno/index.html", {"posts": posts, "categories": categories})


class IndexView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"


class PostView(DetailView, FormView):
    model = Post
    template_name = "bueno/single-post.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_object(self, queryset=None):
        return Post.objects.get(slug=self.kwargs["slug"])

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        print(self.request.POST)
        return super().post(request, *args, **kwargs)

    def form_invalid(self, form):
        print(form.errors)
        return super().form_invalid(form)

    def form_valid(self, form):
        if "main" in self.request.POST:
            print("got here")
            form = CommentForm(self.request.POST)
            parent = None
        else:
            parent = Comment.objects.get(pk=int(self.request.POST["comment_id"]))

        comment = form.save(commit=False)
        comment.post = self.object
        comment.parent = parent
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        return resolve_url("bpost", slug=self.get_object().slug)
