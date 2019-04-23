from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers

from empresa_service import views

router = routers.DefaultRouter()
router.register(r'empresas', views.EmpresasViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #url('^/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
