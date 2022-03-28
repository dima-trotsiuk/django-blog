from django.db import models
from django.db.models import Avg
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    text = models.TextField()
    author = models.CharField(max_length=255, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True)


    def __str__(self):
        return f"{self.pk} - {self.title}"

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'post_id': self.pk})



class Comment(models.Model):
    text = models.TextField()
    publish_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=255)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.pk} - {self.text}"


class Category(models.Model):
    title = models.CharField(max_length=60)

    def __str__(self):
        return f"{self.pk} - {self.title}"


class Feedback(models.Model):
    text = models.TextField()
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    rating = models.IntegerField()



    def __str__(self):
        return f"{self.pk} - {self.text}"
