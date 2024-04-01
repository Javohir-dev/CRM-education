from django.urls import path

from apps.views.home import home_page

urlpatterns = [
    path("", home_page, name="home"),
]
