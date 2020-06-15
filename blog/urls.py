from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", index, name="index"),
    path("post/<slug:slug>", PostView.as_view(), name="post"),
    path("contact/", contact, name="contact"),
    path("category/<slug:slug>", CategoryView.as_view(), name="category"),
    path("categories/", categories, name="category_list"),
    path("tag/<slug:slug>", TagView.as_view(), name="tag"),

]
