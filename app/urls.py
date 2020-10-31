from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_handler, name='index'),
    path('internship/', views.internship_handler, name="internship"),
    path('internship/<int:id>', views.internship_description_handler, name="internship_desctiption"),
    path('open_source/', views.open_source_handler, name='open_source'),
    path('open_source/<int:id>', views.open_source_description_handler, name="open_source_description"),
    path('register/', views.register_handler, name='register'),
]