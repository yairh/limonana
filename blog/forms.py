from django.forms import *
from blog.models import *


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "body", "email")
