from django.urls import path

from api import views
from api.views import LoginAPI, RegisterAPI
from knox import views as knox_views
from api.serializers import ChangePasswordView, UserAPI

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),
    path('product-list/', views.showAll, name='product-list'),
    path('product-detail/<int:pk>', views.viewProduct, name='product-detail'),
    path('product-create/', views.createProduct, name='product-create'),
    path('product-update/<int:pk>', views.updateProduct, name='product-update'),
    path('product-delete/<int:pk>', views.deleteProduct, name='product-delete'),
    
    
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('user/', UserAPI.as_view(), name='user'),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]