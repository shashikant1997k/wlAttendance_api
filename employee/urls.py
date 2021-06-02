
from django.urls import path
# from .views import Register, EmployeeList, EmployeeDetail
from .views import EmployeeDetails, EmployeeList

urlpatterns = [
    path('register/', EmployeeList.as_view(), name="register"),
    path('employeeList/<int:id>/', EmployeeDetails.as_view(), name="employeeList"),
]


# urlpatterns = [
#     # register todo get, post
#     path('register/', EmployeeList.as_view()),
#     # register todo put, patch delete
#     path('employee-list/<int:pk>', EmployeeDetail.as_view()),
# ]
