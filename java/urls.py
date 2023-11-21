from java.views import *
from django.urls import path
 
app_name='anything'
urlpatterns=[
    path('java/',java,name='java'),
     path('java1/',java1,name='java1'),

]