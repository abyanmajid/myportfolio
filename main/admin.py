from re import A
from django.contrib import admin
from .models import Project, Image, Change, FeaturedWork, Education, Skill


class ImageAdmin(admin.StackedInline):
    model = Image

class LessonAdmin(admin.ModelAdmin):
    inlines = [ImageAdmin]

    class Meta:
        model = Project
        
admin.site.register(Image)
admin.site.register(Project)
admin.site.register(Change)
admin.site.register(FeaturedWork)
admin.site.register(Education)
admin.site.register(Skill)