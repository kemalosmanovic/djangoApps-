from django.urls import path
from users import views as user_views
from . import views

urlpatterns =[
    path('', views.home, name='itreporting-home'),
    path('about', views.about, name='itreporting-about'),
    path('contact', views.contact, name='itreporting-contact'),
    path('register/', user_views.register, name='register'),
]
