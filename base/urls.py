from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.studinfo, name= ""),
    path('studresp/<int:pk>', views.studresp, name= ""),
    path('studresplist', views.studresplist, name= "")
]
