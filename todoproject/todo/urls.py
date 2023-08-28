from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name='home'),
    path("create_todo/", views.add_items, name='create'),
    path("view_todo/", views.view_items, name='view')
]