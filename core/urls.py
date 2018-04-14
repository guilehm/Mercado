from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('registro/', views.registro, name='registro'),
    path('produtos/', views.produtos, name='produtos'),
    path('pedidos/', views.pedidos, name='pedidos'),
    path('venda/<int:venda_pk>/', views.venda, name='venda'),
]