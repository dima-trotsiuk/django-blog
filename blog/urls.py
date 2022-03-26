from django.urls import path
from .views import post_list, post_detail, post_new, post_edit, post_delete, post_draft, post_to_publish, \
    posts_by_category

urlpatterns = [
    path('', post_list, name='post_list'),
    path('post/<int:post_id>', post_detail, name='post_detail'),
    path('post/new', post_new, name='post_new'),
    path('post/edit/<int:post_id>', post_edit, name='post_edit'),
    path('post/delete/<int:post_id>', post_delete, name='post_delete'),
    path('post/draft', post_draft, name='post_draft'),
    path('post/post_to_publish/<int:post_id>', post_to_publish, name='post_to_publish'),
    path('posts/category/<int:category_id>', posts_by_category, name='posts_by_category'),
]
