from django.shortcuts import render
from . models import Category,Post,Comment
# Create your views here.

def category_index(request):
    posts=Post.objects.all().order_by('-created')
    context={
        'posts':posts
    }
    return render(request,'blogs/category.html',context)


def blog_category(request,category):
    posts=Post.objects.filter(categories__name__contains=category).order_by('-created')

    context={
        'category':category,
        'posts':posts
    }
    return render(request,'blogs/blog_category.html',context)

from .forms import CommentForm

def blog_detail(request,pk):
    post=Post.objects.get(pk=pk)

    form=CommentForm()
    if request.method=='POST':
        form=CommentForm(request.POST)
        if form.is_valid():
            comment=Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments=Comment.objects.filter(post=post)
    context={
        'post':post,
        'comments':comments
    }
    return render(request,'blogs/blog_detail.html',context)
