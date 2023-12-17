from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from datetime import datetime


class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )

    pub_date = models.DateTimeField(default=datetime.now(), blank=True)
    content = models.TextField()
    category = models.CharField(max_length=40, blank=True, null=True)
    image = models.URLField(null=True, blank=True)
    likes = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("news:detail-story", kwargs={"id":self.id})

class NewsCategory(models.Model):
    name = models.CharField(default = "No category", max_length=50)
    
class NewsComment(models.Model):
    class Meta:
        ordering = ['date']

    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    story = models.ForeignKey(NewsStory,
        related_name="comments",
        on_delete=models.CASCADE
   )
    text = models.TextField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '{}. Posted by {} on {}'.format(self.text,self.author,self.date)
