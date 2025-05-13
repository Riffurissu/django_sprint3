from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post, Category

def get_published_posts():
    return (
        Post.objects.filter(
            is_published=True,
            pub_date__lte=timezone.now(),
            category__is_published=True
        )
        .select_related('author', 'category', 'location')
        .order_by('-pub_date')
    )

def index(request):
    template = 'blog/index.html'
    posts = get_published_posts()[:5]
    context = {'post_list': posts}
    return render(request, template, context)

def post_detail(request, post_id):
    template = 'blog/detail.html'
    post = get_object_or_404(
        Post.objects.select_related('author', 'category', 'location'),
        pk=post_id,
        is_published=True,
        pub_date__lte=timezone.now(),
        category__is_published=True,
    )
    context = {'post': post}
    return render(request, template, context)

def category_posts(request, category_slug):
    template = 'blog/category.html'
    category = get_object_or_404(Category, slug=category_slug, is_published=True)
    posts = (
        Post.objects.filter(
            category=category,
            is_published=True,
            pub_date__lte=timezone.now()
        )
        .select_related('author', 'category', 'location')
        .order_by('-pub_date')
    )
    context = {'category': category, 'post_list': posts}
    return render(request, template, context)
