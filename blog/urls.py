from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path("<int:post_id>/", views.post_detail, name="post_detail"),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('moments/', views.moments_list, name='moments_list'),
    path('moments/<int:moment_id>/', views.moment_detail, name='moment_detail'),
    # path('moments/<int:moment_id>/media/<int:media_id>/', views.moment_detail, name='moment_detail'),

    
]