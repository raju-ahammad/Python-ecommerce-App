from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_save
from .utils import unique_slug_generator
from django.urls import reverse
from django.conf import settings


class BlogCategory(models.Model):
    name  =  models.CharField(max_length=120)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    title       = models.CharField(max_length=120)
    slug        = models.SlugField(blank=True, null=True, unique=True)
    category    = models.ForeignKey(BlogCategory, on_delete=models.CASCADE)
    body        = models.TextField()
    author      = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    publish     = models.DateTimeField(default=timezone.now)
    created     = models.DateTimeField(auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True)
    image       = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("blog_detail", kwargs={'pk': self.pk})

class CommentModel(models.Model):
    content    = models.TextField()
    author     = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True)
    post       = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content






def blog_post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(blog_post_pre_save_receiver, sender=BlogPost)
