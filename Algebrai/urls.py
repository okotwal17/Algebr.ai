from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from Algebrai.views import HomeView  # Import your HomeView from Algebrai app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/')),  # Redirect to login page
    path('accounts/', include('accounts.urls')),  # Include the accounts app URL
    path('home/', HomeView.as_view(), name='home'),  # Add your custom HomeView
]
