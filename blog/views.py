
from django.shortcuts import render, redirect,get_object_or_404
from .models import Post
from .forms import BlogForm
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def blog_list(request):
    posts = Post.objects.all()
   
    return render(request, 'blog_list.html', {'posts': posts})

def create_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
            return redirect('blog_list')
    else:
        form = BlogForm()

    return render(request, 'create_blog.html', {'form': form})

def blog_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog_detail.html', {'post': post})