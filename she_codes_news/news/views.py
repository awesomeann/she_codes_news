from typing import Any
from django.db import models
from django.views import generic
from .models import NewsStory, NewsCategory, NewsComment
from django.urls import reverse_lazy, reverse
from .forms import StoryForm, CommentForm
from django.shortcuts import get_object_or_404, redirect, render
from users.models import CustomUser



# INDEX

class IndexView(generic.ListView):
    template_name = 'news/index.html'
    context_object_name = "all_stories"

    def get_queryset(self):
         selected_author = self.request.GET.get('author')
         if selected_author:
            author = CustomUser.objects.filter(username=selected_author).first()
            return NewsStory.objects.filter(author=author)
         else:
            return NewsStory.objects.all().order_by('-pub_date')[4:]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['latest_stories'] = NewsStory.objects.all().order_by('-pub_date')[:4]
        context['users'] = CustomUser.objects.order_by("username")
        context['selected_author'] = self.request.GET.get('author')
        return context
    
   


#STORIES

# <-- DETAIL VIEW -->

class StoryView(generic.DetailView):
    model = NewsStory
    template_name = 'news/story.html'
    context_object_name = 'story'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context ['form'] = CommentForm()
        return context

# <-- CREATE VIEW -->

class AddStoryView(generic.CreateView):
    form_class = StoryForm 
    context_object_name = 'storyform'
    template_name = 'news/createStory.html'
    success_url = reverse_lazy('news:index')  

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
 # <-- UPDATE VIEW -->   

class StoryEditView(generic.UpdateView):
    template_name = 'news/editStory.html'
    # form_class = StoryForm
    model = NewsStory
    fields = ['title', 'content']
    success_url = reverse_lazy('news:index') 
    


class StoryDeleteView(generic.DeleteView):
    model = NewsStory
    template_name = "news/deleteStory.html"
    content = ['title', 'content']
    success_url = reverse_lazy('news:index') 
    context_object_name = 'story'

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(NewsStory, pk=pk)
    
    def get_succful_url(self):
        return reverse('news:index')
    
# COMMENTS

class AddCommentView(generic.CreateView):
    form_class = CommentForm 

    def get(self, request, *args, **kwargs):
        return redirect("news:story", pk=self.kwargs.get("pk"))
    
    def form_valid (self, form):
        form.instance.author = self.request.user
        pk = self.kwargs.get("pk")
        form.instance.story = get_object_or_404(NewsStory, pk=pk)
        return super().form_valid(form)
    
    def get_success_url(self) :
        return reverse_lazy('news:story', kwargs={'pk':self.kwargs.get("pk")})

class CommentsView(generic.ListView):
    template_name = 'news/story.html'
    context_object_name = "all_comments"

    def get_queryset(self):
        '''Return all news stories.'''
        return NewsComment.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['all_comments'] = NewsComment.objects.all().order_by('-date')
        return context



# class AuthorNewsListView(generic.ListView):
#     template_name = "news/news_by_author.html"

#     def filter_news(username):
#        return NewsStory.objects.filter(publisher__name=username)

#     def get_queryset(self):
#         self.author = get_object_or_404( name=self.kwargs["username"])
#         return NewsStory.objects.filter (publisher=self.publisher)
    
#     def get_context_data(self, **kwargs):
#         context = CustomUser.objects.get(id=self.kwargs['pk'])


    


