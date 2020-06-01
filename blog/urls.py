from django.urls import path
from blog.views import *

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<slug:slug>", PostView.as_view(), name="post"),


]
