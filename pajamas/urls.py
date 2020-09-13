from django.contrib import admin
from django.urls import path
from website import views
from django.urls import re_path, include



urlpatterns = [
    path('admin/', admin.site.urls),  
    path('', views.index),
    path('about/', views.about),
    path('post/', views.post),
    path('offers/', views.offers),
    path('post/<int:id>/', views.post, name='post'),
    path('summernote/', include('django_summernote.urls')),
]
