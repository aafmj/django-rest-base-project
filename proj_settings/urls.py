"""proj_settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from decouple import config
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

from rest_framework.authtoken import views
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    # basic
    path('', RedirectView.as_view(pattern_name='swagger-ui'), name='go-to-swagger'),  # redirect to swagger address
    path('admin/', admin.site.urls),

    # django rest auth
    # path('api-auth/', include('rest_framework.urls')),  # for browsable api
    path('rest-auth/', views.obtain_auth_token),  # POST API to get token


    # apps
    path('user/', include('user.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += [
        # drf_spectacular APIs for documentations
        path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
        path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
        path('redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    ]


admin.site.site_header = config('PROJECT_NAME', default='PROJECT_NAME')
admin.site.site_title = config('PROJECT_NAME', default='PROJECT_NAME')
admin.site.index_title = config('PROJECT_NAME', default='PROJECT_NAME')
