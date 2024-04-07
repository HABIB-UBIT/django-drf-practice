from . import views
from django.urls import path, include

urlpatterns = [
    path('studentapi/', views.studentapi.as_view(), name= ""),
    path('studentapi/<int:pk>', views.studentapi.as_view(), name= "")
]