from django import forms
from .models import Post, Comment, Reply

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text']
        labels = {'title': 'Title', 'author': 'Author', 'text': 'Text'}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['post', 'name', 'email', 'text']
        labels = {'post': 'post', 'name': 'name', 'email': 'email', 'text': 'text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['name', 'text']
        labels = {'name': 'name', 'text': 'text'}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}