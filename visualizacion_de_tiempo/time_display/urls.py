from django.urls import path		
from . import views

urlpatterns=[ 
    path ('', views.root),
    path ('time_display', views.index),
    #path ('otrocon/<variable>',views.nombredeotrafuncion)
]