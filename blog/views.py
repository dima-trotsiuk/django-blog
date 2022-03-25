from datetime import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Post, Comment
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published=True).all()
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = Comment.objects.filter(post=post_id)
    count_comments = comments.count()
    return render(request, 'blog/post_detail.html',
                  {'post': post, 'comments': comments, 'count_comments': count_comments})


def post_new(request):
    if request.method == "GET":
        form = PostForm
        return render(request, 'blog/post_new.html', {'form': form})
    else:
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
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
            post.created_date = datetime.now()
            post.publish_date = datetime.now()
            post.save()
            return redirect('post_detail', post_id=post.pk)


def post_delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id).delete()
    return redirect('post_list')


def post_draft(request):
    posts_draft = Post.objects.filter(published=False).all()
    return render(request, 'blog/post_list.html', {'posts': posts_draft})


def post_to_publish(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.published = True
    post.save()
    return render(request, 'blog/post_detail.html', {'post': post})
