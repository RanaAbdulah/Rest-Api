from django.urls import path
from . import views

urlpatterns = [
    path('public/register/', views.PublicRigisterView.as_view(), name= 'public_register_list'),
    path('public/login/', views.PublicLoginView.as_view(), name= 'public_login_list'),
    path('admin/register/', views.AdminRegisterView.as_view(), name= 'admin_register_list'),
    path('admin/login/', views.AdminLoginView.as_view(), name= 'admin_login_list'),
]