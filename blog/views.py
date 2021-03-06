from django.shortcuts import render, resolve_url, redirect
from django.views.generic import ListView, DetailView, FormView
from blog.models import Post, Category, Comment, Tag
from blog.forms import CommentForm
from django.core.mail import send_mail
from limonana.settings import EMAIL_HOST_USER


# Create your views here.
def index(request):
    posts = Post.objects.filter(status=1).all()
    categories = Category.objects.all()
    return render(request, "index.html", {"posts": posts, "categories": categories})


def contact(request):
    categories = Category.objects.all()
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        content = request.POST.get("message")
        message = f"Message from {name}:{email}:\n{content}"

        send_mail(
            f'Email from {name} on Limonana',
            f'{message}',
            EMAIL_HOST_USER,
            ['odeliagh@gmail.com'],
            fail_silently=False,
        )

        return redirect("contact")

    return render(request, "contact.html", {"categories": categories})


def about(request):
    return render(request, "about.html")


def categories(request):
    categories = Category.objects.all()
    return render(request, "category.html", {"categories": categories})


class IndexView(ListView):
    model = Post
    template_name = "index.html"
    context_object_name = "posts"


class CategoryView(DetailView):
    model = Category
    template_name = "category-post.html"
    context_object_name = "category"

    def get_object(self, queryset=None):
        return Category.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class TagView(DetailView):
    model = Tag
    template_name = "tag-post.html"
    context_object_name = "tag"

    def get_object(self, queryset=None):
        return Tag.objects.get(slug=self.kwargs["slug"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


class PostView(DetailView, FormView):
    model = Post
    template_name = "single-post.html"
    context_object_name = "post"
    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

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
        return resolve_url("post", slug=self.get_object().slug)
