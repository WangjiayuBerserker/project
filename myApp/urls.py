from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^(\d+)/(\d+)/$',views.detail),
    url(r'^grades/$',views.grades),
    url(r'^students/$',views.students),
    url(r'^grades/(\d+)/$',views.gradesStudents),
    url(r'^addstudent/$',views.addstudent),
    url(r'^addstudent2/$',views.addstudent2),
    url(r'^studentsSex/$',views.studentsSex),
    url(r'^studentsNum/$',views.studentsNum),
    url(r'^studentSearch/$',views.studentSearch),
    url(r'^gradesAge/$',views.gradesAge),
    url(r'^stu/(\d+)/$',views.stupage),
]