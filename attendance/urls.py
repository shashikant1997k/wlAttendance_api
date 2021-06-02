
from django.urls import path
from .views import AttendanceInput, AttendanceList, FetchAttendance

urlpatterns = [
    path('attendanceInput/', AttendanceInput.as_view(), name="attendanceInput"),
    path('attendanceList/<int:id>/',
         AttendanceList.as_view(), name="attendanceList"),
    path('fetchAttendance/',
         FetchAttendance.as_view(), name="fetchAttendance"),

]


# urlpatterns = [
#     # register todo get, post
#     path('register/', EmployeeList.as_view()),
#     # register todo put, patch delete
#     path('employee-list/<int:pk>', EmployeeDetail.as_view()),
# ]
