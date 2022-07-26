from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('works/', views.all_works, name='all_works'),
	path('works/<int:id>/', views.work, name='work'),
]