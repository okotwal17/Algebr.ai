from django.views.generic import TemplateView
from django.template import loader
from django.shortcuts import render  # Import render
from django.http import HttpResponse
import ollama

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
class PracticeTestView(TemplateView):
    template_name = 'practiceTest.html'

    def generate_ai_question(self, difficulty, topic):
        """Generate a question based on difficulty."""
        response = ollama.chat(model='gemma:2b', messages=[{
            'role': 'user',
            'content': f'Generate a {difficulty} algebra question with the topic of {topic}. Just provide the question without any additional text.'
        }])
        return response['message']['content']

    def get_ai_answer(self, question):
        """Get the answer to the question."""
        response = ollama.chat(model='gemma:2b', messages=[{
            'role': 'user',
            'content': f'Solve this algebra question: {question}. Provide the explanation and steps you took to solve it.'
        }])
        return response['message']['content']

    def post(self, request, *args, **kwargs):
        question_number = int(request.POST.get('question_number', 1))
        question_difficulty = request.POST.get('question_difficulty', 'Easy')
        correct_count = int(request.POST.get('correct_count', 0))
        total_questions = int(request.POST.get('total_questions', 10))
        topic = request.POST.get('topic', '')

        # Check if grading is submitted
        if 'grade' in request.POST:
            if request.POST['grade'] == 'correct':
                correct_count += 1
                if question_difficulty == 'Easy':
                    question_difficulty = 'Medium'
                elif question_difficulty == 'Medium':
                    question_difficulty = 'Hard'
                else:
                    question_difficulty = 'Hard'
            question_number += 1


        # Generate new question if not at the end
        if question_number <= total_questions:
            question_on_screen = self.generate_ai_question(question_difficulty, topic)
            correct_answer = self.get_ai_answer(question_on_screen)

            context = {
                'question_text': question_on_screen,
                'correct_answer': correct_answer,
                'question_number': question_number,
                'correct_count': correct_count,
                'total_questions': total_questions,
                'difficulty': question_difficulty,
                'topic': topic,
                'user_answer': '',  # Clear the user answer for the next question
            }

            return render(request, self.template_name, context)
        else:
            return render(request, 'results.html', {'correct_count': correct_count, 'total_questions': total_questions})

        
        # If the test is completed, show results        
    def get(self, request, *args, **kwargs):
        topic = request.GET.get('topic', '')
        total_questions = int(request.GET.get('total_questions', 10))  # Default to 10 if not specified
        question_difficulty = 'Easy'  # Start with easy questions
        question_text = self.generate_ai_question(question_difficulty, topic)
        correct_answer = self.get_ai_answer(question_text)

        return render(request, self.template_name, {
            'question_text': question_text,
            'question_number': 1,
            'correct_answer': correct_answer,
            'correct_count': 0,
            'total_questions': total_questions,
            'difficulty': question_difficulty,
            'user_answer': ''
        })


class ResultsView(TemplateView):
    template_name = 'results.html'  # Specify the template for the results

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))
