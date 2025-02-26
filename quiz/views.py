from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Question, Answer, Resource

def quiz_home(request):
    questions = Question.objects.all()
    return render(request, 'quiz/home.html', {'questions': questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(request, 'quiz/detail.html', {'question': question})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signing up
            return redirect('quiz_home')  # Redirect to the home page
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def quiz_home(request):
    questions = Question.objects.all()
    return render(request, 'quiz/home.html', {'questions': questions})