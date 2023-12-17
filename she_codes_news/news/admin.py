from django.contrib import admin
from .models import NewsComment, NewsCategory, NewsStory

admin.site.register(NewsCategory)
admin.site.register(NewsComment)
admin.site.register(NewsStory)