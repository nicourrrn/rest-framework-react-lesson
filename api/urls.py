from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 


urlpatterns = [
    path('project/', views.ProjectList.as_view()),
    path('project/<int:pk>', views.ProjectDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
