from django.urls import path
from .views import home, about, get_form, success, report


urlpatterns = [
    path("", home, name="home"),
    path("about/", about, name="about"),
    path("add/", get_form, name="get_form"),
    path("success/<int:mood_id>", success, name="success"),
    path('report/', report, name='report'),
    
]