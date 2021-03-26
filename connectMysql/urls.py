"""connectMysql URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include

from rest_framework.documentation import include_docs_urls
from rest_framework_swagger.views import get_swagger_view  # <-- Here
schema_view = get_swagger_view(title='swagger docs')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),


    path('docs/', schema_view),  # <-- Here
    # path('', include('jac_api.urls')),
    # path('', include('obj_api.urls')),
    # path('ui/', include('ui.urls')),
    # path('ui/', include('django.contrib.auth.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from rest_framework_swagger.views import get_swagger_view  # <-- Here

# schema_view = get_swagger_view(title='Jaseci API')

# urlpatterns = [
#     path('api/', include('api.urls')),
#     path('api-auth/', include('rest_framework.urls')),
#     path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
#     path('docs/', schema_view),  # <-- Here
#     path('admin/', admin.site.urls),
#     path('user/', include('user_api.urls')),
#     path('', include('jac_api.urls')),
#     path('', include('obj_api.urls')),
#     path('ui/', include('ui.urls')),
#     path('ui/', include('django.contrib.auth.urls')),
# ]