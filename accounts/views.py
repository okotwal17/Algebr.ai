from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib import messages

class CustomLoginView(LoginView):
    template_name = 'login.html'  # Specify your login template

    def form_valid(self, form):
        # Call the parent class's form_valid method
        response = super().form_valid(form)
        # Add success message after a successful login
        messages.success(self.request, self.get_success_message(form.cleaned_data))
        return response

    def get_success_url(self):
        return reverse_lazy('home')  # Redirect to the home page after login

    def get_success_message(self, cleaned_data):
        return "Welcome back, {}!".format(cleaned_data.get("username"))  # Optional success message after login

    def form_invalid(self, form):
        messages.error(self.request, "Invalid username or password.")
        return super().form_invalid(form)

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')  # Redirect to login page after logout
