from django.shortcuts import render
from .models import BlogPost


# Create your views here.
def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs' : blogs})

def blog_detail(request, pk):
    blog = BlogPost.objects.get(id=pk)
    return render(request, 'blog/blog_detail.html', {'blog' : blog})

def blog_category(request, category):
    blogs = BlogPost.objects.filter(tags__contains=[category])
    return render(request, 'blog/blog_list.html', {'blogs' : blogs})
    
