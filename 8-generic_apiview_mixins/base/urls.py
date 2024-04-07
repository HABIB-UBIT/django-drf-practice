from . import views
from django.urls import path, include


######## SEPERATELY #########

# urlpatterns = [
#     path('studentapi/', views.studentlist.as_view(), name= ""),
#     path('studentapicreate/', views.studentcreate.as_view(), name= ""),
#     path('studentapiretrieve/<int:pk>', views.studentretrieve.as_view(), name= ""),
#     path('studentapiupdate/<int:pk>', views.studentupdate.as_view(), name= ""),
#     path('studentapidestroy/<int:pk>', views.studentdestroy.as_view(), name= ""),
# ]


######## COMBINED #########

urlpatterns = [
    path('studentapi/', views.studentlistandcreate.as_view(), name= ""),
    path('studentapi/<int:pk>', views.updatedeleteretrievestudent.as_view(), name= ""),
]
