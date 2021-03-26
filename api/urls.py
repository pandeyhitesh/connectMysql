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


    path('csa-all/', views.showAllCsaUser, name='product-detail'),
    path('create-csa-user/', views.createCsaUser, name='create-csa-user'),
    path('csa-user-view/<int:user_id>', views.viewCsaUser, name='view-csa-user'),
    path('csa-user-update/<int:user_id>', views.updateCsaUser, name='update-csa-user'),
    path('csa-user-delete/<int:user_id>', views.deleteCsaUser, name='delete-csa-user'),


    path('student-all/', views.showAllStudents, name='view-all-students'),
    path('create-student/', views.createStudent, name='create-student'),
    path('student-view/<int:user_id>', views.viewStudent, name='view-student'),
    path('student-update/<int:user_id>', views.updateStudent, name='update-student'),
    path('student-delete/<int:user_id>', views.deleteStudent, name='delete-student'),
    
    path('notice-all/', views.showAllNotices, name='view-all-notices'),
    path('create-notice/', views.createNotice, name='create-notice'),
    path('notice-view/<int:notice_id>', views.viewNotice, name='view-notice'),
    # path('student-update/<int:user_id>', views.updateStudent, name='update-student'),
    path('notice-delete/<int:notice_id>', views.deleteNotice, name='delete-notice'),

    
    path('events-all/', views.showAllEvents, name='view-all-events'),
    path('create-event/', views.createEvent, name='create-event'),
    path('event-view/<int:event_id>', views.viewEvent, name='view-event'),
    # path('event-update/<int:user_id>', views.update, name='update-student'),
    path('event-delete/<int:event_id>', views.deleteEvent, name='delete-event'),

    
    path('project-all/', views.showAllProjects, name='view-all-projects'),
    path('create-project/', views.createProject, name='create-project'),
    path('project-view/<int:user_id>', views.viewProject, name='view-project'),
    path('project-update/<int:user_id>', views.updateProject, name='update-project'),
    path('project-delete/<int:user_id>', views.deleteProject, name='delete-project'),
    
]