from django.urls import path		
from . import views

urlpatterns=[ 
    path ('', views.root),
    path ('time_display', views.index),
    path ('datetime', views.time)
    #path ('otrocon/<variable>',views.nombredeotrafuncion)
]