from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Task, Category
# Create your views here.


# *************************************category*************************************


class CategoryListView(ListView):
    model = Category
    template_name = 'todo/show_categories.html'
    context_object_name = "categories"

    def get_queryset(self):
        queryset = {'empty_list': Category.categories.empty_categories().all(),
                    'non_empty_list': Category.categories.non_empty_categories().all()}
        return queryset


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'todo/category_detail.html'


class CategoryUpdateView(UpdateView):
    model = Category
    fields = ('name',)
    template_name = 'todo/category_edit.html'


class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'todo/category_delete.html'
    success_url = reverse_lazy('category_list')


class CategoryCreateView(CreateView):
    model = Category
    template_name = 'todo/category_new.html'
    fields = ('name',)


# *************************************task*************************************


class TaskListView(ListView):
    model = Task
    template_name = 'todo/show_tasks.html'
    context_object_name = "tasks"


class SeparatedTaskListView(ListView):
    model = Task
    template_name = 'todo/show_separated_tasks.html'
    context_object_name = "tasks"

    def get_queryset(self):
        queryset = {'expired_list': Task.tasks.expired_tasks().all(),
                    'non_expired_list': Task.tasks.non_expired_tasks().all()}
        return queryset


class TaskDetailView(DetailView):
    model = Task
    template_name = 'todo/task_detail.html'


class TaskCreateView(CreateView):
    model = Task
    template_name = 'todo/task_new.html'
    fields = ('title', 'description', 'priority', 'category', 'due_date', 'done')


class TaskUpdateView(UpdateView):
    model = Task
    fields = ('title', 'description', 'priority', 'category', 'due_date', 'done')
    template_name = 'todo/task_edit.html'


class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'todo/task_delete.html'
    success_url = reverse_lazy('task_list')
