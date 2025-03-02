from django.views.generic import TemplateView
from django.template import loader
from django.shortcuts import render  # Import render
from django.http import HttpResponse
from openai import OpenAI

import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Now use the OpenAI API key from the .env file
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)


# Home page view
class HomeView(TemplateView):
    template_name = 'home.html'  # Specify your home template

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user  # Pass the user to the template
        return context

    def get(self, request, *args, **kwargs):
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
    template_name = 'simplifyingAlgebraExp.html'  # Specify the template for simplifying algebra expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class GraphLinearEqView(TemplateView):
    template_name = 'graphingLinearEquations.html'  # Specify the template for graphing linear equations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))


class SystemsOfEquationsView(TemplateView):
    template_name = 'systemsOfEquations.html'  # Specify the template for systems of equations

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class PolynomialsView(TemplateView):
    template_name = 'polynomials.html'  # Specify the template for polynomials

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))


class RationalExpressionsView(TemplateView):
    template_name = 'rationalExpressions.html'  # Specify the template for rational expressions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))


class InequalitiesView(TemplateView):
    template_name = 'inequalities.html'  # Specify the template for inequalities

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

class ExponentialFunctionsView(TemplateView):
    template_name = 'exponentialFunctions.html'  # Specify the template for exponential functions

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))

# View for the Practice Test page

from django.shortcuts import render
from django.views.generic import TemplateView
from django.utils.html import escape
import re


class PracticeTestView(TemplateView):
    template_name = 'practiceTest.html'

    def generate_ai_question(self, difficulty, topic):
        """Generate a question based on difficulty and topic."""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert math question generator."},
                {
                    "role": "user",
                    "content": f"Generate a {difficulty} algebra question with the topic of {topic}. "
                               "Only provide the question text, no explanations or additional text. Make sure that there are no dollar signs when rendering.",
                },
            ],
        )
        return response.choices[0].message.content.strip()

    def get_ai_answer(self, question):
        """Get the answer to the generated question."""
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert math problem solver."},
                {
                    "role": "user",
                    "content": f"Solve this algebra question: {question}. "
                               "and explain in at most 2 sentences.",
                },
            ],
        )
        return response.choices[0].message.content.strip()

    def format_latex(self, content):
        """Convert raw LaTeX to MathJax-friendly escaped HTML."""
        def replace_fraction(match):
            numerator, denominator = match.groups()
            return f"\\frac{{{numerator}}}{{{denominator}}}"

        # Escape other content and format fractions
        escaped_content = escape(content)
        return re.sub(r"frac\{(\d+)\}\{(\d+)\}", replace_fraction, escaped_content)

    def post(self, request, *args, **kwargs):
        """Handle form submissions."""
        # Extract form data
        question_number = int(request.POST.get('question_number', 1))
        question_difficulty = request.POST.get('question_difficulty', 'Easy')
        correct_count = int(request.POST.get('correct_count', 0))
        total_questions = int(request.POST.get('total_questions', 10))
        topic = request.POST.get('topic', '')
        user_answer = request.POST.get('user_answer', '')

        # Handle grading logic
        if 'grade' in request.POST:
            if request.POST['grade'] == 'correct':
                correct_count += 1
                if question_difficulty == 'Easy':
                    question_difficulty = 'Medium'
                elif question_difficulty == 'Medium':
                    question_difficulty = 'Hard'
            question_number += 1

        # Check if test is complete
        if question_number > total_questions:
            return render(request, 'results.html', {'correct_count': correct_count, 'total_questions': total_questions})

        # Generate next question
        question_text = self.generate_ai_question(question_difficulty, topic)
        correct_answer = self.get_ai_answer(question_text)

        # Format for MathJax
        question_text = self.format_latex(question_text)
        correct_answer = self.format_latex(correct_answer)

        # Prepare context for the template
        context = {
            'question_text': question_text,
            'correct_answer': correct_answer,
            'question_number': question_number,
            'correct_count': correct_count,
            'total_questions': total_questions,
            'difficulty': question_difficulty,
            'topic': topic,
            'user_answer': user_answer,  # Preserve user input
        }
        return render(request, self.template_name, context)

    def get(self, request, *args, **kwargs):
        """Start a new test."""
        # Initialize test parameters
        topic = request.GET.get('topic', 'Algebra')
        total_questions = int(request.GET.get('total_questions', 10))  # Default: 10 questions
        question_difficulty = 'Easy'
        question_text = self.generate_ai_question(question_difficulty, topic)
        correct_answer = self.get_ai_answer(question_text)

        # Format for MathJax
        question_text = self.format_latex(question_text)
        correct_answer = self.format_latex(correct_answer)

        # Prepare initial context
        context = {
            'question_text': question_text,
            'question_number': 1,
            'correct_answer': correct_answer,
            'correct_count': 0,
            'total_questions': total_questions,
            'difficulty': question_difficulty,
            'topic': topic,
            'user_answer': '',  # Start fresh
        }
        return render(request, self.template_name, context)


class ResultsView(TemplateView):
    template_name = 'results.html'  # Specify the template for the results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))
