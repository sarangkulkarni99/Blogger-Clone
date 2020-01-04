from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.title



class Comment(models.Model):
    """Comments to the post"""
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return 'Comment {} by {}'.format(self.text, self.name)

class Reply(models.Model):
    """Reply to a comment"""
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    date_added = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    class Meta:
        ordering = ['-date_added']
        verbose_name_plural = 'replies'

    def __str__(self):
        return 'Reply {} by {}' .format(self.text, self.name)