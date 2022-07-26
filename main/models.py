from xml.sax.handler import feature_external_ges
from django.db import models
from datetime import date
import PIL.Image

# Project
class Project(models.Model):
    title = models.CharField(max_length=250)
    developer = models.CharField(max_length=250, default='Abyan Majid')
    description = models.TextField()
    professional = models.BooleanField()
    url = models.URLField(max_length=400, blank=True)
    category = models.CharField(max_length=20, blank=True)
    release_date = models.DateField(default=date.today)
    featured_image_650x650 = models.ImageField(upload_to='images/', blank=True)

    def __str__(self):
        return self.title

# Images of a specific project
class Image(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=False)
    
    def save(self, *args, **kwargs):
       super(Image, self).save(*args, **kwargs)
       img = PIL.Image.open(self.image.path)
       if img.height > 1080 or img.width > 1920:
           img.thumbnail((1920, 1080))
       img.save(self.image.path,quality=70,optimize=True)

# Changelog for a specific project
class Change(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    version = models.CharField(max_length=15, blank=False)
    changes = models.CharField(max_length=250, blank=False)
    release_date = models.DateField(default=date.today, blank=False)
    
    def __str__(self):
        return self.version

# Works Featured in Home Page
class FeaturedWork(models.Model):
    featured_work1_title = models.CharField(max_length=100, blank=False)
    featured_work2_title = models.CharField(max_length=100, blank=False)
    featured_work3_title = models.CharField(max_length=100, blank=False)
    featured_work4_title = models.CharField(max_length=100, blank=False)
    featured_work5_title = models.CharField(max_length=100, blank=False)
    featured_work6_title = models.CharField(max_length=100, blank=False)

# Education listed in Home Page
class Education(models.Model):
    featuredwork = models.ForeignKey(FeaturedWork, on_delete=models.CASCADE)
    school = models.CharField(max_length=200, blank=False)
    education = models.CharField(max_length=200, blank=False)

# Skills listed in Home Page
class Skill(models.Model):
    featuredwork = models.ForeignKey(FeaturedWork, on_delete=models.CASCADE)
    skill = models.CharField(max_length=200)