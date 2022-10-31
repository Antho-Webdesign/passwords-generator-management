from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

CATEGORY_CHOICES = (
    ('site vitrine', 'site_vitrine'),
    ('application web', 'application_web'),
    ('application mobile', 'application_mobile'),
    ('autres', 'Other'),
)

PROJECT_STATUS = (
    ('active', 'Active'),
    ('inactive', 'Inactive'),
    ('completed', 'Completed'),
)


class Category(models.Model):
    project_category = models.CharField(max_length=120, blank=True, null=True)
    category_name = models.CharField(max_length=120, blank=True, null=True)
    slug = models.SlugField(max_length=120, blank=True, null=True)
    image_cat = models.ImageField(upload_to='images/portfolio/category',
                                  default='images/portfolio/category/default.jpg')
    description_cat = models.TextField(max_length=2500, blank=True, null=True)

    def __str__(self):
        return self.project_category

    def get_absolute_url(self):
        return reverse('project_category_list', kwargs={'slug': self.slug})

    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ['project_category']


class Project(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    description = models.TextField()
    date_created_on = models.DateTimeField(auto_now_add=True)
    project_status = models.CharField(choices=PROJECT_STATUS, default='active', max_length=30)
    project_thumbnail = models.ImageField(upload_to='images/portfolio/project/',
                                          default='images/portfolio/project/default.jpg')
    project_url = models.URLField(max_length=200, default='#')
    category = models.CharField(choices=CATEGORY_CHOICES, default='site vitrine', max_length=20, blank=True, null=True)
    category_fk = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Projects'
        verbose_name = 'Project'
        ordering = ['-date_created_on']

    def get_absolute_url(self):
        return reverse('category_list', kwargs={'slug': self.slug})



