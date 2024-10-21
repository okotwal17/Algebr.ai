# views.py
from django.shortcuts import render
import ollama  # Import your Ollama library

def generate_ai_question(difficulty):
    """Generate a question based on difficulty using Gemma 2B."""
    response = ollama.chat(model='gemma:2b', messages=[
        {
            'role': 'user',
            'content': f'Generate a {difficulty} algebra question.'
        },
    ])
    return response['message']['content']  # Extract the generated question

def get_ai_answer(question):
    """Get the answer to the question using Gemma 2B."""
    response = ollama.chat(model='gemma:2b', messages=[
        {
            'role': 'user',
            'content': f'Solve this algebra question: {question}.'
        },
    ])
    return response['message']['content']  # Extract the answer

def practice_test(request):
    """Handles the practice test view and question generation."""
    if request.method == 'POST':
        user_answer = request.POST['user_answer']
        question_number = int(request.POST['question_number'])
        question_difficulty = request.POST['question_difficulty']
        correct_answer = request.POST['correct_answer']
        correct_count = int(request.POST['correct_count'])

        # Check if answer is correct
        is_correct = user_answer.strip() == correct_answer.strip()
        if is_correct:
            correct_count += 1
        
        # Update difficulty based on correctness
        difficulty = 'easy' if not is_correct else 'medium' if question_difficulty == 'easy' else 'hard'
        
        # Generate next question
        next_question = generate_ai_question(difficulty)
        next_correct_answer = get_ai_answer(next_question)

        # Update question number and check if test is over
        total_questions = int(request.POST['total_questions'])
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

    # On GET request, initialize first question
    total_questions = 10  # Set this dynamically if needed
    question_difficulty = 'easy'  # Start with easy questions
    question_text = generate_ai_question(question_difficulty)
    correct_answer = get_ai_answer(question_text)

    return render(request, 'practiceTest.html', {
        'question_text': question_text,
        'question_number': 1,
        'correct_answer': correct_answer,
        'correct_count': 0,
        'total_questions': total_questions,
        'difficulty': question_difficulty
    })
