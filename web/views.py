from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from web.models import ToDo
from web.forms import ToDoModelForm
from django.urls import reverse


class ToDoCreateView(CreateView):
    model = ToDo
    form_class = ToDoModelForm

    def get_success_url(self):
        return reverse('web:todo_detail', args=(self.object.id,))


class ToDoUpdateView(UpdateView):
    model = ToDo
    form_class = ToDoModelForm

    def get_success_url(self):
        return reverse('web:todo_detail', args=(self.object.id,))


class ToDoDeleteView(DeleteView):
    model = ToDo

    def get_success_url(self):
        return reverse('web:todo_list')


class ToDoListView(ListView):
    model = ToDo
    ordering = ['-id']


class ToDoDetailView(DetailView):
    model = ToDo
