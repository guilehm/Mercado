from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('registro/', views.registro, name='registro'),
    path('produtos/', views.produtos, name='produtos'),
    path('pedidos/', views.pedidos, name='pedidos'),
]