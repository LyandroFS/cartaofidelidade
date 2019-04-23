"""cartaofidelidade URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.urls import logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appcartaofidelidade.urls')),
   # path('restapi', include('api.urls')),
    path('cliente_service/v1/', include('cliente_service.urls')),
    path('empresas_service/v1/', include('empresa_service.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url('^/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^logout/$', logout, {'next_page': '/login/'}, name='logout'),
]
