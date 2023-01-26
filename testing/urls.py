"""testing URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from api.routers.urls import router
from django.conf.urls.static import static
from django.views.generic import RedirectView



urlpatterns = [
    path('admin/', admin.site.urls),
    # На сервере появилась ошибка с прошлого семестра, поэтому вписал следующие 3 строки (ака Q запрос)
    # path('', RedirectView.as_view(url='/main/', permanent=True)),
    # path('polls/', RedirectView.as_view(url='/main/', permanent=True)),
    # path('main/', include('main.urls')),
    path('', include('main.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
