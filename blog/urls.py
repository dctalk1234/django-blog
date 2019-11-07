from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('blogs/<int:pk>', views.blog_detail, name='blog_detail'),
    path('blogs/new', views.blog_create, name='blog_create'),
    path('blogs/<str:category>', views.blog_category, name='blog_category'),
    path('blogs/<int:pk>/delete', views.blog_delete, name='blog_delete'),
    path('blogs/<int:pk>/edit', views.blog_edit, name='blog_edit'),

]