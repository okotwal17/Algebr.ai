from django.shortcuts import render

# Create your views here.

# accounts/views.py

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Specify your login template
    success_url = reverse_lazy('home')  # Redirect to a home page after login
    def form_invalid(self, form):
            messages.error(self.request, "Invalid username or password.")
            return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout

# accounts/views.py

from django.shortcuts import render

def login_view(request):
    return render(request, 'login.html')  # This should match your template filename

