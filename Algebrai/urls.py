from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from Algebrai.views import HomeView, SolvingLinearEqView, QuadraticEquationsView, FactoringExpressionsView, SimplAlgExpView # Import the new views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/')),  # Redirect to login page
    path('accounts/', include('accounts.urls')),  # Include the accounts app URL
    path('home/', HomeView.as_view(), name='home'),  # Home page view
    
    # Algebra topic URLs
    path('solving-linear-equations/', SolvingLinearEqView.as_view(), name='solvingLinearEq'),  # Solving Linear Equations page
    path('quadratic-equations/', QuadraticEquationsView.as_view(), name='quadraticEquations'),  # Quadratic Equations page
    path('factoring-expressions/', FactoringExpressionsView.as_view(), name='factoringExpressions'),  # Corrected name
    path('simplifying-Algebra-expressions/', SimplAlgExpView.as_view(), name='simplifyingAlgebraExp'),  # Corrected name


    # Add more paths for other algebra topics as needed
]
