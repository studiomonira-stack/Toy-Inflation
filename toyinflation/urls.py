from django.contrib import admin
from django.urls import path
from calculator import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('leksaker/', views.toy_list, name='toy_list'),
    path('leksak/<slug:slug>/', views.toy_detail, name='toy_detail'),
    path('blogg/', views.blog_list, name='blog_list'),
    path('blogg/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('ansvar/', views.privacy, name='privacy'),
    path('kontakt/', views.contact, name='contact'),
    path('robots.txt', views.robots_txt, name='robots_txt'),
]