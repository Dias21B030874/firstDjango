from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import TaskForm
from .models import Task


class TaskListView(ListView):
    model = Task
    context_object_name = 'tasks'


class TaskDetailView(DetailView):
    model = Task


class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    login_url = reverse_lazy('tasks:signin')
    success_url = reverse_lazy('tasks:task_list')


class TaskUpdateView(LoginRequiredMixin, UpdateView):
    model = Task
    form_class = TaskForm
    login_url = reverse_lazy('tasks:signin')
    success_url = reverse_lazy('tasks:task_list')


class TaskDeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    login_url = reverse_lazy('tasks:signin')
    success_url = reverse_lazy('tasks:task_list')


class SimpleLoginView(LoginView):
    template_name = 'registration/signin.html'


class SimpleSignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('tasks:signin')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        response = super().form_valid(form)
        next_url = self.request.GET.get('next')
        if next_url:
            self.success_url = next_url
        return response


class SimpleLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'
