from django.conf.urls import url

#from django.urls import path   #THIS IS TO BE USED FOR PATH
from first_app import views

urlpatterns=[
    #path('',views.index,name='index'),  ###PATH
    url(r'^$',views.index,name='index'),

]
