from django.urls import path
from . import views

urlpatterns=[
    path('',views.login_usuario, name='home'),
    path('login/',views.login_usuario, name='login_usuario'),
    path('dashboard/',views.dashboard, name='dashboard_usuario'),
    path('logout/',views.logout, name='logout'),
    path('cadastro/',views.cadastro_usuario, name='cadastro_usuario'),
]