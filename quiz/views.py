from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Question, Answer, Resource

def home(request):
    return render(request, 'quiz/home.html')

def quiz_page(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz_page.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    correct_answers = question.answer_set.filter(is_correct=True)
    user_is_correct = False
    selected_answers = []

    if request.method == 'POST':
        selected_answers = request.POST.getlist('answer')  # Get selected answer IDs
        selected_answers = [int(answer_id) for answer_id in selected_answers]

        # Check if all correct answers are selected and no incorrect answers are selected
        correct_answer_ids = list(correct_answers.values_list('id', flat=True))
        if set(selected_answers) == set(correct_answer_ids):
            user_is_correct = True
            messages.success(request, "Congratulations! You got it right! 🎉")
        else:
            messages.warning(request, "That's not quite right. Please review the resources below to improve your understanding.")
        
    return render(request, 'quiz/detail.html', {
        'question': question,
        'user_is_correct': user_is_correct,
        'selected_answers': selected_answers,
    })
        
def contact(request):
    return render(request, 'quiz/contact.html')

# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log the user in after signing up
#             return redirect('quiz_home')  # Redirect to the home page
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})