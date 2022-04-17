# code adopted from https://github.com/gomathishankar28/ms4_bubbles/tree/main/blog
from django.db import models
from profiles.models import UserProfile


class Blog(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.title


class Post(models.Model):
    blog = models.ForeignKey(Blog, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    author = models.CharField(max_length=255)
    intro = models.TextField()
    article = models.TextField()
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    comment_desc = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return '%s - %s - %s' % (self.post.title, self.name, self.date_added)
