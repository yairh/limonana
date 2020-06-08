from django.forms import *
from blog.models import *
from django_summernote.widgets import SummernoteWidget


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ("name", "email", "body")

        widgets = {"body": Textarea(attrs={"class": "form-control"}),
                   "email": EmailInput(attrs={"class": "form-control"}),
                   "name": TextInput(attrs={"class": "form-control"})}


commentform_factory = formset_factory(CommentForm)
