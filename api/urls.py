from django.urls import path, include
from . import views 


urlpatterns = [
    path('project/', views.project_list),
    path('project/<int:pk>', views.project_detail),
]
