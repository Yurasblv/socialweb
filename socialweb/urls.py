from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.title_page, name="title"),
    path("guests/", views.all_guests_page, name="guests"),
]
