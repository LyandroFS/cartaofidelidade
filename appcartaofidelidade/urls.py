from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = routers.DefaultRouter()
#router.register(r'users', views.UserViewSet)
#router.register(r'groups', views.GroupViewSet)
router.register(r'registros', views.RegistrosViewSet)
router.register(r'servicos', views.ServicosViewSet)
router.register(r'premios', views.PremiosViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    #path('', views.index, name='index'),
    #path('', views.cliente_list, name='cliente_list'),
    #path('cliente/<int:pk>/', views.cliente_detail, name='cliente_detail'),
    #path('cliente/new/', views.cliente_new, name='cliente_new'),
    #path('cliente/<int:pk>/edit/', views.cliente_edit, name='cliente_edit'),



    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),

]