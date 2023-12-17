from typing import Any
from django.db import models
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views import generic
from .models import CustomUser
from .forms import CustomUserCreationForm
from django.shortcuts import get_object_or_404, redirect, render

class CreateAccountView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/createAccount.html'




class ViewAccount(generic.DetailView):
    model = CustomUser
    template_name = 'users/viewAccount.html'
    context_object_name = 'author'
    success_url = reverse_lazy('account')

    def get_object(self):
        pk = self.kwargs.get("pk")
        return get_object_or_404(CustomUser, pk=pk)




   
