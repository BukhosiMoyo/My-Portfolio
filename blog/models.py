from django.db import models
from django.contrib.auth.models import  User
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("update-post-list")
    


class Post(models.Model):


    STATUS_CHOICES = (                                 
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    PreviewImage = models.ImageField(upload_to='PostImage')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    publish_date = models.DateField(auto_now_add=True)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    status = models.CharField( max_length=10, choices=STATUS_CHOICES, default='draft')
    objects = models.Manager()
    published = PublishedManager()
    category = models.CharField(max_length=50, default='uncategorized')

    def __str__(self):
        return self.title + " | " + str(self.author)

    def get_absolute_url(self):
        return reverse("update-post-list")
    

    