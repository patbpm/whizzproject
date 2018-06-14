from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.

def blog(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')

    context = {
        'posts': posts
    }
    return render(request, 'blog/blog.html', context)

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post
    }
    return render(request, 'blog/post_detail.html', context)