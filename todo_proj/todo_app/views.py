from typing import Any
from django.db import models
from django.forms.models import BaseModelForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render,redirect
from . import models
from django.urls import reverse_lazy
# Create your views here.
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,TemplateView
from django.contrib.auth.views import LoginView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
def BaseView(request):
    return render(request,'todo_app/base.html')
class IndexView(TemplateView):
    template_name='todo_app/index.html'
class AboutView(TemplateView):
    template_name='todo_app/about.html'
class ShareView(TemplateView):
    template_name='todo_app/share.html'
class TaskList(LoginRequiredMixin,ListView):
    model=models.Tasks
    context_object_name='tasks'
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        context['tasks']=context['tasks'].filter(user=self.request.user)
        context['tasks']=context['tasks'].order_by('due_at')
        context['count']=context['tasks'].filter(compleated=False).count()
        return context
class TaskDetailView(LoginRequiredMixin,DetailView):
    model=models.Tasks
    context_object_name='task'
    template_name="todo_app/task_detail.html"
class TaskCreateView(LoginRequiredMixin,CreateView):
    model=models.Tasks
    template_name='todo_app/task_create.html'
    fields=['title', 'description', 'due_at','compleated']
    success_url=reverse_lazy('home')
    
    def form_valid(self,form): 
        form.instance.user=self.request.user
        return super(TaskCreateView,self).form_valid(form)
    
class TaskUpdateView(LoginRequiredMixin,UpdateView,SuccessMessageMixin):
    model=models.Tasks
    template_name='todo_app/task_update.html'
    fields='__all__'
    success_message='Task has been updated'
    success_url=reverse_lazy('home')
class TaskDeleteView(LoginRequiredMixin,DeleteView):
     model=models.Tasks
     success_url=reverse_lazy('home')
class UserLoginView(LoginView):
    models=User
    template_name='todo_app/login.html'
    redirect_authenticated_user=True
    
    def get_success_url(self) :
        return reverse_lazy('home')
    
class UserRegisterView(FormView):
    template_name='todo_app/register.html'
    form_class=UserCreationForm
    redirect_authenticated_user=True
    success_url=reverse_lazy('home')
    
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
        return super(UserRegisterView,self).form_valid(form)
    def get(self,*args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super(UserRegisterView,self).get(*args,**kwargs)
    
    
    
    