from django.urls import path
from web.views import ToDoCreateView, ToDoUpdateView, ToDoDeleteView, ToDoListView, ToDoDetailView


app_name = 'web'
urlpatterns = [
    path('', ToDoListView.as_view(), name='todo_list'),
    path('<int:pk>', ToDoDetailView.as_view(), name='todo_detail'),
    path('create', ToDoCreateView.as_view(), name='todo_create'),
    path('<int:pk>/update', ToDoUpdateView.as_view(), name='todo_update'),
    path('<int:pk>/delete', ToDoDeleteView.as_view(), name='todo_delete'),
]
