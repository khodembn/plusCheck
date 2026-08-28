from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views
from .views import (
    home,
    about,
    get_form,
    success,
    report,
)


urlpatterns = [
    
    path("", home, name="home"),
    
    path("about/", about, name="about"),
    
    path("register/", views.register_view, name="register"),

    path(
        "login/",
        LoginView.as_view(template_name="core/login.html"),
        name="login",
    ),

    path(
        "logout/",
        LogoutView.as_view(),
        name="logout",
    ),
    
    path("add/", get_form, name="get_form"),
    path("success/<int:mood_id>/", success, name="success"),
    
    path('report/', report, name='report'),
    
]