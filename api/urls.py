from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 


urlpatterns = [
    path('', views.api_root),

    path('projects/', views.ProjectList.as_view(), name='project-list'),
    path('projects/<int:pk>', views.ProjectDetail.as_view(), name='project-detail'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail'),

    path('api-auth/', include('rest_framework.urls')),
]

urlpatterns = format_suffix_patterns(urlpatterns)
