from django.http import request
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView,FormView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login



class Login(LoginView):
          template_name='todos/login.html'
          fields='__all__'    
          redirect_authenticated_user=True
          def get_success_url(self):
              return reverse_lazy('list')


class Register(FormView):
          template_name='todos/register.html'
          form_class=UserCreationForm
          success_url = reverse_lazy('list')

          def form_valid(self, form):
                    user=form.save()
                    if user is not None:
                              login(self.request,user)
                    return super(Register,self).form_valid(form)

          def get(self,*args, **kwargs):
                    if self.request.user.is_authenticated:
                              return redirect('list')


class TaskList(LoginRequiredMixin,ListView):
          model=Task
          context_object_name='tasks'
          template_name='todos/list.html'

          def get_context_data(self, **kwargs):
              context= super().get_context_data(**kwargs)
              context['tasks']=context['tasks'].filter(user=self.request.user)
              context['count']=context['tasks'].filter(complete=False).count()

              search_input=self.request.GET.get('search_area') or ''
              if search_input:
                        context['tasks']=context['tasks'].filter(title__icontains=search_input)
              context['search_input']=search_input
              return context


                   

          
class DetailList(LoginRequiredMixin,DetailView):
          model=Task
          context_object_name='task'
          template_name='todos/detail.html'



class Create(LoginRequiredMixin,CreateView):
          model=Task
          context_object_name='task'
          template_name='todos/create.html'
          fields=['title','description','complete']
          success_url=reverse_lazy('list')

          def form_valid(self, form):
              form.instance.user=self.request.user
              return super(Create,self).form_valid(form)

class Update(LoginRequiredMixin,UpdateView):
          model=Task
          context_object_name='task'
          template_name='todos/update.html'
          fields='__all__'
          success_url=reverse_lazy('list')

class Delete(LoginRequiredMixin,DeleteView):
          model=Task
          context_object_name='task'
          template_name='todos/delete.html'
          success_url=reverse_lazy('list')
          
