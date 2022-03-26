from django import forms
from django.forms import Textarea

from .models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            "title",
            "text",
            "author",
            "published",
            "category"
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            "text",
        )

        widgets = {
            'text': Textarea(attrs={'rows': 4, 'cols': 40})
        }