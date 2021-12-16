from django.conf import urls
from django.urls import path
from django.urls.resolvers import URLPattern
from django.urls import path

from . import views

urlpatterns = [
    path("students/", views.students, name="students"),
    path("create-student/", views.create_student, name="create_student"),
    path("login/", views.login_request, name="login"),
    path("register/", views.register, name="register"),
    path("", views.index, name="index"),
]