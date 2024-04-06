from . import views
from django.urls import path, include

urlpatterns = [
    path('studentapi/', views.studentapi, name= ""),
    path('studentapi/<int:pk>', views.studentapi, name= "")
]