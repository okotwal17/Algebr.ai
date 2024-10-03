from django.urls import path
from .views import CustomLoginView, CustomLogoutView  

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),  # URL for login page
    path('logout/', CustomLogoutView.as_view(), name='logout'), 
]
