from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='inicio'),
    path('clientes/editar/<int:cliente_id>/', views.editar_cliente, name='editar_cliente'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path('medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
    path('medicamentos/<int:medicamento_id>/', views.detalle_medicamento, name='detalle_medicamento'),
    path('medicamentos/alta/', views.alta_medicamento, name='alta_medicamento'),
    path('medicamentos/login/', views.login, name='login'),
    path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
    path('medicamentos/<int:medicamento_id>/editar/', views.editar_medicamento, name='editar_medicamento'),
    path('pedido/', views.cargar_pedido, name='pedido'),
    path('medicamento/<int:pk>/eliminar/', views.eliminar_medicamento, name='eliminar_medicamento'),
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('proveedores/', views.lista_proveedores, name='lista_proveedores'),
    path('alta_cliente/', views.alta_cliente, name='alta_cliente'),
    path('eliminar_cliente/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('alta_proveedor/', views.alta_proveedor, name='alta_proveedor'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile_view, name='profile'),
    path('accounts/login/', views.login,name='login'),   
     path('proveedores/eliminar/', views.eliminar_proveedor, name='eliminar_proveedor'),
]