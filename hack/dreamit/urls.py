from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("contact/", views.contact, name="contact"),
    path("content/", views.content, name="content"),
    path("sign/", views.sign, name="sign"),
    path("signin/", views.signin, name="signin"),
    path("signout/", views.signout, name="signout"),
]