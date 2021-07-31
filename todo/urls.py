from django.urls import path
from .views import TaskListView, TaskDetailView, \
    CategoryListView, CategoryDetailView, SeparatedTaskListView, \
    TaskUpdateView, TaskDeleteView, CategoryDeleteView, \
    CategoryUpdateView, TaskCreateView, CategoryCreateView

urlpatterns = [
    # task
    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('separated-tasks/', SeparatedTaskListView.as_view(), name='separated_task_list'),
    path('new-task/', TaskCreateView.as_view(), name='new_task'),
    path('task/<slug:slug>/', TaskDetailView.as_view(), name='task_detail'),
    path('task/<slug:slug>/edit/', TaskUpdateView.as_view(), name='task_edit'),
    path('task/<slug:slug>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    # category
    path('categories/', CategoryListView.as_view(), name='category_list'),
    path('new-category/', CategoryCreateView.as_view(), name='new_category'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<slug:slug>/edit/', CategoryUpdateView.as_view(), name='category_edit'),
    path('category/<slug:slug>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
]
