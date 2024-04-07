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

# urlpatterns = [
#     path('studentapi/', views.ListCreateStudent.as_view(), name= ""),
#     path('studentapiru/<int:pk>', views.RetrieveUpdateStudent.as_view(), name= "retrieve-update"),
#     path('studentapird/<int:pk>', views.RetrievedestroyStudent.as_view(), name= "retrieve-destroy"),
#     path('studentapirud/<int:pk>', views.RetrieveupdatedestroyStudent.as_view(), name= "retrieve-update-destroy"),

# ]


######## Most Important and Easy to make CRUD function #########

urlpatterns = [
    path('studentapi/', views.ListCreateStudent.as_view(), name= ""),
    path('studentapi/<int:pk>', views.RetrieveUpdateDestroyStudent.as_view(), name= "retrieve-update-destroy")
]