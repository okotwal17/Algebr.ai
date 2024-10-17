from django.views.generic import TemplateView
from django.template import loader
from django.http import HttpResponse

# Home page view
class HomeView(TemplateView):
    template_name = 'home.html'  # Specify your home template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the user to the template
        return context

    def get(self, request, *args, **kwargs):
        # Check the template loading
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)  # Get context data
        return HttpResponse(template.render(context, request))  # Render the template with context

# View for "Solving Linear Equations" page
class SolvingLinearEqView(TemplateView):
    template_name = 'solvingLinearEq.html'  # Specify the template for solving linear equations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

# View for "Quadratic Equations" page
class QuadraticEquationsView(TemplateView):
    template_name = 'quadraticEquations.html'  # Specify the template for quadratic equations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class FactoringExpressionsView(TemplateView):
    template_name = 'factoringExpressions.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class SimplAlgExpView(TemplateView):
    template_name = 'simplifyingAlgebraExp.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class GraphLinearEqView(TemplateView):
    template_name = 'graphingLinearEquations.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))


class SystemsOfEquationsView(TemplateView):
    template_name = 'systemsOfEquations.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))
    
class PolynomialsView(TemplateView):
    template_name = 'polynomials.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))
    

class RationalExpressionsView(TemplateView):
    template_name = 'rationalExpressions.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))
    

class InequalitiesView(TemplateView):
    template_name = 'inequalities.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class ExponentialFunctionsView(TemplateView):
    template_name = 'exponentialFunctions.html'  # Specify the template for factoring expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))