from . import views
from django.urls import path, include




urlpatterns = [
    path('studentapi/', views.StudentViewSet.as_view(), name= ""),
]