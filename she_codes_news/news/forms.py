from django import forms
from django.forms import ModelForm
from .models import NewsStory, NewsComment


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory 
        fields = ['title',  'content', 'image']
        

class CommentForm(ModelForm):
    class Meta:
        model = NewsComment
        fields = ['text']
        

    