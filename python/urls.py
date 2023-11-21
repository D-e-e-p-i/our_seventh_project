from python.views import *

from django.urls import path 
app_name='something'

urlpatterns=[
    path('python/',python,name='python'),
    path('python1/',python1,name='python1'),
    
]