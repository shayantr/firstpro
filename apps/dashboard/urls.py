from django.urls import path

from . import views

app_name="dashboard"

urlpatterns = [
    path("", views.index, name='index'),
    path("<str:name>", views.dashboard, name="dashboard")
]
