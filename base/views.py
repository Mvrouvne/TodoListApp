from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Task

########## Handling login ##########

class   HandleLogin(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasklist')

######################################

class   TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

class   TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'details'
    # template_name = 'base/task.html'

class   TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasklist')

class   TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasklist')

class   TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'delete'
    success_url = reverse_lazy('tasklist')