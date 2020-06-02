from django.urls import path
from blog.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/<slug:slug>", PostView.as_view(), name="post"),
    path("bueno/", index, name="bueno"),
    path("bueno/<slug:slug>", PostView.as_view(), name="bpost"),

]
