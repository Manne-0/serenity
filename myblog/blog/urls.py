from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
]