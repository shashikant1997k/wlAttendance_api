from django.urls import path
from .views import Register, Login, Logout

urlpatterns = [
    path('userLogin/', Login.as_view(), name="userLogin"),
    path('userRegister/', Register.as_view(), name="userRegister"),
    path('userLogout/', Logout.as_view(), name="userLogout"),
]
