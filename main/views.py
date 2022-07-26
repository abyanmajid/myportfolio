from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.core.mail import EmailMessage, BadHeaderError
from .models import Project, FeaturedWork, Education, Skill
from datetime import date
from django.conf import settings

def home(response):
    # Featured Works
    featuredwork1 = Project.objects.get(title=FeaturedWork.objects.get(id=1).featured_work1_title)
    featuredwork2 = Project.objects.get(title=FeaturedWork.objects.get(id=1).featured_work2_title)
    featuredwork3 = Project.objects.get(title=FeaturedWork.objects.get(id=1).featured_work3_title)
    featuredwork4 = Project.objects.get(title=FeaturedWork.objects.get(id=1).featured_work4_title)
    featuredwork5 = Project.objects.get(title=FeaturedWork.objects.get(id=1).featured_work5_title)
    featuredwork6 = Project.objects.get(title=FeaturedWork.objects.get(id=1).featured_work6_title)
    
    # My Education
    educations = Education.objects.all()
    
    # My Skill
    skills = Skill.objects.all()
    
    # My Age
    today = date.today()
    age = today.year - 2005 - ((today.month, today.day) < (9, 19))
    
    context = {
        'age': age,
        'educations': educations,
        'skills': skills,
        'featuredwork1': featuredwork1,
        'featuredwork2': featuredwork2,
        'featuredwork3': featuredwork3,
        'featuredwork4': featuredwork4,
        'featuredwork5': featuredwork5,
        'featuredwork6': featuredwork6,
        }
    return render(response, 'main/index.html', context)

def all_works(response):
    all_works = Project.objects.all()
    professional = []
    sideprojects = []
    
    for project in all_works:
        if project.professional == True:
            professional.append(project)
        else:
            sideprojects.append(project)
    context = {
        'professional': professional,
        'sideprojects': sideprojects,
    }
    return render(response, 'main/all_works.html', context)

def work(response, id):
    work = Project.objects.get(id=id)
    images = work.image_set.all()
    changelog = work.change_set.all()
    context = {
        'work': work,
        'images': images,
        'changelog': changelog,
        }
    return render(response, 'main/work.html', context)