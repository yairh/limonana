from django.db.models import *
from django.contrib.auth.models import User
from stdimage import StdImageField, JPEGField

STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Profile(Model):
    user = OneToOneField(User, on_delete=CASCADE)
    avatar = ImageField(upload_to="avatars/", default="avatars/Logo-carre-transparent.png")
    bio = TextField(default="")

    def __str__(self):
        return self.user.username


class Category(Model):
    name = CharField(max_length=60)
    slug = SlugField(unique=True, null=True)
    image = ImageField(upload_to="category-img/", default="category-img/logo_carre_VF.png")

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=60)
    slug = SlugField(unique=True,null=True)

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
    intro = TextField(null=True)
    created_on = DateTimeField(auto_now_add=True)
    status = IntegerField(choices=STATUS, default=0)
    image = StdImageField(upload_to="title-img/", null=True,
                          variations={"squared_image": {'width': 500, 'height': 500},
                                      'thumbnail': {'width': 100, 'height': 75}})

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


class CommentManager(Manager):
    def all(self):
        """Return results of instance with no parent (not a reply)."""
        qs = super().filter(parent=None)
        return qs


class Comment(Model):
    post = ForeignKey(Post, on_delete=CASCADE, related_name='comments')
    name = CharField(max_length=80)
    email = EmailField(default="somemail@limonana.com")
    body = TextField(verbose_name="Text")
    created_on = DateTimeField(auto_now_add=True)
    active = BooleanField(default=False)
    parent = ForeignKey("self", on_delete=CASCADE, null=True, blank=True)

    objects = CommentManager()

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)

    def children(self):
        """Return replies of a comment."""
        return Comment.objects.filter(parent=self)

    def children_count(self):
        return self.children().count()
