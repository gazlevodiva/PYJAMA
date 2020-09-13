from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Post


def index(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    context = {"res": request, 'posts': posts}
    return render(request, "index.html", context)


def about(request):
    return render(request, "about.html")


def post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {"res": request, 'post': post}
    return render(request, "post.html", context)


def offers(request):
    return render(request, "offers.html")