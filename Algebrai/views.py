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

    def generate_ai_question(self, difficulty):
        """Generate a question based on difficulty."""
        response = ollama.chat(model='gemma:2b', messages=[
            {'role': 'user', 'content': f'Generate a {difficulty} algebra question. Just provide the question without any additional text.'}
        ])
        return response['message']['content']

    def get_ai_answer(self, question):
        """Get the answer to the question."""
        response = ollama.chat(model='gemma:2b', messages=[
            {'role': 'user', 'content': f'Solve this algebra question: {question}. Provide just the answer without any explanation.'}
        ])
        return response['message']['content']

    def post(self, request, *args, **kwargs):
        user_answer = request.POST.get('user_answer', '')
        question_number = int(request.POST.get('question_number', 1))
        question_difficulty = request.POST.get('question_difficulty', 'easy')
        correct_answer = request.POST.get('correct_answer', '')
        correct_count = int(request.POST.get('correct_count', 0))

        # Debugging output to verify answers
        print(f"User Answer: '{user_answer}', Correct Answer: '{correct_answer}'")

        # Check if answer is correct, ensuring consistent formatting
        is_correct = user_answer.strip().lower() == correct_answer.strip().lower()
        
        if is_correct:
            correct_count += 1
            difficulty = 'medium' if question_difficulty == 'easy' else 'hard' if question_difficulty == 'medium' else 'hard'
        else:
            difficulty = 'easy' if question_difficulty == 'easy' else 'easy' if question_difficulty == 'medium' else 'hard'

        # Generate next question
        next_question = self.generate_ai_question(difficulty)
        next_correct_answer = self.get_ai_answer(next_question)

        # Update question number and check if test is over
        total_questions = int(request.POST.get('total_questions', 10))
        question_number += 1

        if question_number > total_questions:
            return render(request, 'results.html', {'correct_count': correct_count, 'total_questions': total_questions})

        return render(request, 'practiceTest.html', {
            'question_text': next_question,
            'question_number': question_number,
            'correct_answer': next_correct_answer,
            'correct_count': correct_count,
            'total_questions': total_questions,
            'difficulty': difficulty,
            'is_correct': is_correct
        })



    def get(self, request, *args, **kwargs):
        total_questions = 10  # Set this dynamically if needed
        question_difficulty = 'easy'  # Start with easy questions
        question_text = self.generate_ai_question(question_difficulty)
        correct_answer = self.get_ai_answer(question_text)

        return render(request, self.template_name, {
            'question_text': question_text,
            'question_number': 1,
            'correct_answer': correct_answer,
            'correct_count': 0,
            'total_questions': total_questions,
            'difficulty': question_difficulty
        })


class ResultsView(TemplateView):
    template_name = 'results.html'  # Specify the template for the practice test

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        template = loader.get_template(self.template_name)
        context = self.get_context_data(**kwargs)
        return HttpResponse(template.render(context, request))
