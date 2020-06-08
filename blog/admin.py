from django.contrib import admin
from .models import Post, Comment, Category, Tag, Profile
from django.db.models import TextField
from tinymce.widgets import AdminTinyMCE
from django.forms import *
from django.contrib.admin.widgets import AdminTextareaWidget


class PostAdminForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        widgets = {"intro": AdminTextareaWidget(), "content": AdminTinyMCE()}


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminForm


#
# class PostAdmin(SummernoteModelAdmin):
#     summernote_fields = ('content',)


admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Profile)
