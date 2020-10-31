from django.urls import path
from django.conf.urls.static import static 
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from . import views
from devNITH import settings


urlpatterns = [
    path('', views.index_handler, name='index'),
    path('internship/', views.internship_handler, name="internship"),
    path('open_source/', views.open_source_handler, name='open_source'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.Register.as_view(), name='signup'),
]