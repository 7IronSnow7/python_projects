from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("verify/", views.verify_security, name="verify_security")
]
