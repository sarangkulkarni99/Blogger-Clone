from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from .forms import CommentForm, ReplyForm
from .models import Post, Comment
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.urls import reverse
# Create your views here.


def index(request):
    """Home page for blogs"""
    return render(request, 'index.html')

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-date_added')
    template_name = 'posts.html'
    paginate_by = 3

def post_comments(request, post_id):
    """Show comments of a post"""
    try:
        post = get_object_or_404(Post, id=post_id)
        comments = post.comment_set.all()
    except Post.NoReverseMatch:
        raise Http404
    context = {'post': post, 'comments': comments}
    return render(request, 'post_comments.html', context)


@login_required
def new_comment(request, post_id):
    """Add a new comment to a post"""
    post = Post.objects.get(id=post_id)

    if request.method != 'POST':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(reverse('blogs:post_detail',
                                                args=[post_id]))

    context = {'post': post, 'form': form}
    return render(request, 'new_comment.html', context)

def replies(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    reply = comment.reply_set.all()
    context = {'comment': comment, 'reply': reply}
    return render(request, 'replies.html', context)

@login_required
def reply(request, comment_id):
    """Add a reply to a comment"""
    comment = get_object_or_404(Comment, id=comment_id)

    if request.method != 'POST':
        form = ReplyForm()
    else:
        form = ReplyForm(data=request.POST)
        if form.is_valid():
            new_reply = form.save(commit=False)
            new_reply.comment = comment
            new_reply.save()
            return HttpResponseRedirect(reverse('blogs:replies',
                                                args=[comment_id]))

    context = {'comment': comment, 'form': form}
    return render(request, 'reply.html', context)