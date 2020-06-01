from django.db.models import *
from django.contrib.auth.models import User

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Category(Model):
    name = CharField(max_length=60)

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=60)

    def __str__(self):
        return self.name


class Post(Model):
    title = CharField(max_length=200, unique=True)
    slug = SlugField(max_length=200, unique=True)
    category = ForeignKey(Category, on_delete=SET_NULL, null=True)
    tags = ManyToManyField(Tag)
    author = ForeignKey(User, on_delete=CASCADE, related_name='posts')
    updated_on = DateTimeField(auto_now=True)
    content = TextField()
    created_on = DateTimeField(auto_now_add=True)
    status = IntegerField(choices=STATUS, default=0)
    image = ImageField(upload_to="title-img/", null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    name = CharField(max_length=80)
    email = EmailField()
    body = TextField()
    created_on = DateTimeField(auto_now_add=True)
    active = BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)
