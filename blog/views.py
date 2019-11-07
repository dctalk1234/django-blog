from django.shortcuts import render, redirect
from .models import BlogPost

from .forms import BlogPostForm

from django.contrib.auth.decorators import login_required

# Create your views here.
def blog_list(request):
    blogs = BlogPost.objects.all().order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'blogs' : blogs})

def blog_detail(request, pk):
    blog = BlogPost.objects.get(id=pk)
    return render(request, 'blog/blog_detail.html', {'blog' : blog})

def blog_category(request, category):
    blogs = BlogPost.objects.filter(tags__contains=[category])
    return render(request, 'blog/blog_list.html', {'blogs' : blogs})

@login_required
def blog_create(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm
    
    return render(request, 'blog/blog_form.html', {'form' : form})

@login_required
def blog_edit(request, pk):
    blog_post = BlogPost.objects.get(pk=pk)

    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            blog_post = form.save()
            return redirect('blog_detail', pk=blog_post.pk)
    else:
        form = BlogPostForm(instance=blog_post)
    
    return render(request, 'blog/blog_form.html', {'form' : form})

@login_required
def blog_delete(request, pk):
    BlogPost.objects.get(id=pk).delete()
    return redirect('blog_list')
