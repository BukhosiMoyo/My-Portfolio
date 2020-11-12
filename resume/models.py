from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms 
from django.core.validators import MaxValueValidator, MinValueValidator


class Person(models.Model):

    AVAILABILITY = (
        ('Available', 'Available '),
        ('Unavailable', 'Unavailable')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    display_name = models.CharField(null=True, max_length=50)
    age = models.IntegerField(null= True)
    health = models.CharField(null=True, default='Excellent', max_length=50)
    phone = models.CharField(null=True, max_length=31)
    email = models.EmailField(null=True, max_length=200)
    profilePicture = models.ImageField(upload_to="img")
    address = models.CharField(null=True, max_length=200)
    nationality = models.CharField(null=True, max_length=50)
    religion = models.CharField(null=True, max_length=200)
    skype = models.CharField(null=True, max_length=50)
    freelance = models.CharField(null=True, max_length=50, choices=AVAILABILITY)
    languages = models.CharField(null=True, max_length=200)
    description = models.TextField(null=True, max_length=250)
    resume = models.FileField(upload_to="files/resume")  
    

    def __str__(self):
        return str(self.display_name)

class Skill(models.Model):
    LEVEL = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
        ('Expert', 'Expert')
    )

    name = models.CharField(null=True, max_length=500)
    badge = models.CharField(null=True, max_length=50, choices=LEVEL)
    level = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)])

    def __str__(self):
        return self.name


class Experience(models.Model):

    name = models.CharField(null=True, max_length=50)
    company = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=500)
    current = models.BooleanField(null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)    

    def __str__(self):
        return self.name

class Education(models.Model):

    name = models.CharField(null=True, max_length=50)
    school = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, max_length=500)
    current = models.BooleanField(null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)

    def __str__(self):
        return self.name

class Stat(models.Model):


    name = models.CharField( null=True ,max_length=50)
    years_of_experience = models.IntegerField(null=True)
    projects_completed = models.IntegerField(null=True)
    happy_clients = models.IntegerField(null=True)
    awards_won = models.IntegerField(null=True)
    
    def __str__(self):
        return self.name
    
class ImagePortfolio(models.Model):

    project_name = models.CharField(null=True, max_length=150)
    client = models.CharField(null=True, max_length=150)
    technologies = models.CharField(null=True, max_length=150)
    preview_link = models.URLField(null=True, max_length=200)
    portfolio_image = models.ImageField(null=True, upload_to="img", default="placeholder.png")

    def __str__(self):
        return self.project_name
    

class SliderPortfolio(models.Model):
    project_name = models.CharField(null=True, max_length=150)
    client = models.CharField(null=True, max_length=150)
    technologies = models.CharField(null=True, max_length=150)
    preview_link = models.URLField(null=True, max_length=200)
    preview_image = models.ImageField(null=True, upload_to="img/slider",)
    portfolio_image1 = models.ImageField(null=True, upload_to="img/slider",)
    portfolio_image2 = models.ImageField(null=True, upload_to="img/slider",)
    portfolio_image3 = models.ImageField(null=True, upload_to="img/slider",)
    portfolio_image4 = models.ImageField(null=True, upload_to="img/slider",)
    

    def __str__(self):
        return self.project_name


class LocalVideoPortfolio(models.Model):
    project_name = models.CharField(null=True, max_length=150)
    client = models.CharField(null=True, max_length=150)
    technologies = models.CharField(null=True, max_length=150)
    video_file = models.FileField(upload_to='static/LocalVideos', max_length=100)
    preview_link = models.URLField(null=True, max_length=200)
    preview_image = models.ImageField(null=True, upload_to="video/LocalVideoImage",)

    def __str__(self):
        return self.project_name

class YoutubeVideoPortfolio(models.Model):
    project_name = models.CharField(null=True, max_length=150)
    client = models.CharField(null=True, max_length=150)
    technologies = models.CharField(null=True, max_length=150)
    preview_link = models.URLField(null=True, max_length=200)
    youtube_imbed_code = models.CharField(null=True, max_length=1000)
    preview_image = models.ImageField(null=True, upload_to="img/YoutubePreview",)

    def __str__(self):
        return self.project_name

class Social(models.Model):
    SOCIALS = (
        ('github', 'github'),
        ('linkedin', 'linkedin'),
        ('behance', 'behance'),
        ('facebook', 'facebook'),
        ('twitter', 'twitter'),
        ('youtube', 'youtube'),
    )

    name = models.CharField(null=True, max_length=200, choices=SOCIALS)
    social_link = models.URLField(null=True, max_length=200)

    def __str__(self):
        return self.name
    