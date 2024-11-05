from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name="index.html"), name='logout'),

    path('personal_page/', views.personal_page, name='personal_page'),
    path('register_record/', views.register_record, name='register_record'),
]
