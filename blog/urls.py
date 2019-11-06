from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blogs/<str:category>', views.blog_category, name='blog_category'),
]