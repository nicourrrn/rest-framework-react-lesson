from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from . import views 


urlpatterns = [
    path('project/', views.project_list),
    path('project/<int:pk>', views.project_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
