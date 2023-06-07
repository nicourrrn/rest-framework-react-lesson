from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 

project_detail = views.ProjectViewSet.as_view({'get': 'list', 'post': 'create'})

urlpatterns = [
    path('', views.api_root),
    path('old_api/projects', project_detail),
    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),

    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
