from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_handler, name='index'),
    path('internship/', views.internship_handler, name="internship"),
]