from django.contrib import admin
from django.urls import path, include
from stock import views
from django.contrib.auth import views as auth_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'medicamentos', views.MedicamentoViewSet, basename='medicamento')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api', include(router.urls)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('', include('stock.urls')),
    path('logout', auth_views.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('api-auth/', include('rest_framework.urls'))
]







