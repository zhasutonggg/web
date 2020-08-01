from . import views
from django.conf.urls import url
from django.conf import settings
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#from django.contrib import staticfiles
urlpatterns=[
     url(r'^$', views.index),
     url(r'^grades/', views.grades),
     url(r'^students/', views.students),
     url(r'^grades/(\d+)$',views.gradesStudents),
     url(r'^bp',views.bp),
        ]
#urlpatterns += staticfiles_urlpatterns()
