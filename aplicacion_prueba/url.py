from django.urls import path
from .views import Login, Homepage, Register, Logaud , Quiz ,quiz_view, save_quiz
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('<int:pk>', Quiz.as_view(), name='quiz'),
    path('register', Register.as_view(), name='register'),
    path('<int:pk>/data/', quiz_view.as_view(), name='quiz_data'),
    path('<int:pk>/save/', save_quiz.as_view(), name='save_quiz'),
    path('login', Login.as_view(), name='login'),
    path('logaud', Logaud.as_view(), name='logaud')
]