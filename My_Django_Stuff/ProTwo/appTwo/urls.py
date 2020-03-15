from django.conf.urls import url
#from django.urls import path   #THIS IS TO BE USED FOR PATH

from appTwo import views

urlpatterns=[
#    path('',views.help,name='help'),     #PATH
    url(r'^$',views.help,name='help'),
]
