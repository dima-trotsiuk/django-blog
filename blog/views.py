from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm


def post_list(request):
    posts = Post.objects.filter().all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_id)
    count_comments = comments.count()
    if request.method == 'GET':
        form = CommentForm()
    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_form = form.save(commit=False)
            comment_form.post = post
            comment_form.author = request.user
            comment_form.save()
            return redirect('post_detail', post_id=post.pk)
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'comments': comments, 'count_comments': count_comments, 'form': form})


def post_new(request):
    if request.method == "GET":
        form = PostForm
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_detail', post_id=post.pk)


def post_edit(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == "GET":
        form = PostForm(instance=post)  # заповнення старими даними
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)

            post.save()
            return redirect('post_detail', post_id=post.pk)


def post_delete(request, post_id):
    get_object_or_404(Post, pk=post_id).delete()
    return redirect('post_list')


def post_draft(request):
    posts_draft = Post.objects.filter(published=False).all()
    categories = Category.objects.all()

    return render(request, 'blog/post_list.html', {'posts': posts_draft, 'categories': categories})


def post_to_publish(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.published = True
    post.save()
    comments = Comment.objects.filter(post=post_id)
    count_comments = comments.count()
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'comments': comments, 'count_comments': count_comments})


def posts_by_category(request, category_id):
    posts = Post.objects.filter(category_id=category_id).all()
    categories = Category.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts, 'categories': categories})
