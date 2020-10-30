from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_handler, name='index'),
    path('internship/', views.internship_handler, name="internship"),
    path('open_source/', views.open_source_handler, name='open_source'),
]