from django.urls import path, include
from rest_framework.routers import DefaultRouter 

from . import views 

router = DefaultRouter()
router.register(r'projects', views.ProjectViewSet, basename='project')
router.register(r'users', views.UserViewSet, basename='user')

subproj_router = DefaultRouter()
subproj_router.register(r'tasks', views.TaskView, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('projects/<int:projects_pk>/', include(subproj_router.urls)),
    path('auth', views.CustomAuthToken.as_view()),
]

