from django.urls import path
from . import  views

urlpatterns=[
    path('',views.download,name="youtube_Download"),
   # path('download/',views.downloadspage,name="Download"),
]