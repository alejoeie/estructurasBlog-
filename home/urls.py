from django.contrib import admin
from django.urls import path, include
from home import views


#Django admin customization

admin.site.site_header = "Engineers"
admin.site.site_title = "Welcome"
admin.site.site_index = "Welcome to the Jungle"
urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('contact', views.contact, name='contact'),
    path('enthusiasts', views.enthusiasts, name='enthusiasts'),   
    path('curriculum', views.curriculum, name='curriculum'),   
    path('method', views.method, name='method'),   
    path('detector', views.detector, name='detector'),   

]