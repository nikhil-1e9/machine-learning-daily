from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_home, name='quiz_home'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('signup/', views.signup, name='signup'),  # Signup URL
]