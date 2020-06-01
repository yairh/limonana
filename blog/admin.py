from django.contrib import admin
from django.urls import reverse
from .models import Post, Comment, Category, Tag
from django_summernote.admin import SummernoteModelAdmin
from django.db.models import TextField
from tinymce.widgets import AdminTinyMCE


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    formfield_overrides = {
        TextField: {'widget': AdminTinyMCE()},
    }


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
