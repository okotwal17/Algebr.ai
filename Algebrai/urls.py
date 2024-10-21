from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from Algebrai.views import (
    HomeView,
    SolvingLinearEqView,
    QuadraticEquationsView,
    FactoringExpressionsView,
    SimplAlgExpView,
    GraphLinearEqView,
    SystemsOfEquationsView,
    PolynomialsView,
    RationalExpressionsView,
    InequalitiesView,
    ExponentialFunctionsView,
    PracticeTestView,  # Import the new practice test view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/accounts/login/')),  # Redirect to login page
    path('accounts/', include('accounts.urls')),  # Include the accounts app URL
    path('home/', HomeView.as_view(), name='home'),  # Home page view
    
    # Algebra topic URLs
    path('solving-linear-equations/', SolvingLinearEqView.as_view(), name='solvingLinearEq'),  # Solving Linear Equations page
    path('quadratic-equations/', QuadraticEquationsView.as_view(), name='quadraticEquations'),  # Quadratic Equations page
    path('factoring-expressions/', FactoringExpressionsView.as_view(), name='factoringExpressions'),  # Corrected name
    path('simplifying-algebra-expressions/', SimplAlgExpView.as_view(), name='simplifyingAlgebraExp'),  # Corrected name
    path('graphing-linear-equations/', GraphLinearEqView.as_view(), name='graphingLinearEquations'),  # Corrected name
    path('systems-of-equations/', SystemsOfEquationsView.as_view(), name='systemsOfEquations'),  # Corrected name
    path('polynomials/', PolynomialsView.as_view(), name='polynomials'),  # Corrected name
    path('rational-expressions/', RationalExpressionsView.as_view(), name='rationalExpressions'),  # Corrected name
    path('inequalities/', InequalitiesView.as_view(), name='inequalities'),  # Corrected name
    path('exponential-functions/', ExponentialFunctionsView.as_view(), name='exponentialFunctions'),  # Corrected name
    path('practice-test/', PracticeTestView.as_view(), name='practiceTest'),  # Practice Test page
]
