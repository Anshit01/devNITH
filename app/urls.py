from django.urls import path
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from devNITH import settings


urlpatterns = [
    path('', views.index_handler, name='index'),

    path('internship/', views.internship_handler, name="internship"),
    path('internship/<int:id>', views.internship_description_handler, name="internship_desctiption"),
    path('open_source/', views.open_source_handler, name='open_source'),
    path('open_source/<int:id>', views.open_source_description_handler, name="open_source_description"),

    # path('register/', views.register_handler, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='signup'),

    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('add_internship_post/', views.internship_post_form_view, name='add_internship_post'),
    path('add_open_source_post/', views.open_source_post_form_view, name='add_open_source_post'),


]