from . import views
from django.urls import path

urlpatterns = [
    #path('demo/',views.demo,name='demo'),
    #path('about/',views.about,name='about'),
    #path('add/',views.result,name='result')
    path('',views.index1,name='index'),
]
