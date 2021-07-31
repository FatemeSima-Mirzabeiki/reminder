from django.db import models
from django.db.models import Count
# from django.db.models.functions import Now
from django.template.defaultfilters import slugify
from django.utils.timezone import now
from todo.utils import get_random_code
from django.urls import reverse


# Create your models here.


# **********************Category**********************


# this is a manager class
# first method finds categories that have no tasks
# and the another method, finds categories that have tasks...
class CategoryManager(models.Manager):
    def empty_categories(self):
        return self.filter(tasks__isnull=True)

    def non_empty_categories(self):
        return self.annotate(num_task=Count('tasks')).filter(num_task__gt=0)


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, blank=False)
    slug = models.SlugField(unique=True, blank=True)
    # managers
    objects = models.Manager()
    categories = CategoryManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(get_random_code() + "-" + self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', args=[self.slug])


# **********************Task**********************
PRIORITIES = (
    ('H', 'High'),
    ('M', 'Medium'),
    ('L', 'Low')
)


# this is a manager class
# first method finds expired tasks
# and the another method, non-expired tasks...
class TaskManager(models.Manager):
    def expired_tasks(self):
        return self.filter(due_date__lt=now())

    def non_expired_tasks(self):
        return self.filter(due_date__gte=now())


class Task(models.Model):
    class Meta:
        ordering = ['due_date']

    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    due_date = models.DateTimeField(editable=True)
    priority = models.CharField(
        max_length=30,
        choices=PRIORITIES,
        default=PRIORITIES[0][0]
    )
    done = models.BooleanField(default=False)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name='tasks', on_delete=models.CASCADE)
    # managers
    objects = models.Manager()
    tasks = TaskManager()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(get_random_code() + "-" + self.title)
        super(Task, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task_detail', args=[self.slug])

# 888888888888888888888888888888888888888888888888888

# show all task: remaining time moshkel dare

