from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.http import JsonResponse
from .forms import RegiterForm
from django.contrib.auth.admin import User
from .models import Profile, Question, Answers, Forms
from django.core.paginator import Paginator


class Homepage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {'form': Forms.objects.filter(complete=True),
                                              'user': Profile.objects.all()})


class Quiz(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        quiz = Forms.objects.get(pk=pk)
        return render(request, 'Quiz.html', {'quiz': quiz})


class quiz_view(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        quiz = Forms.objects.get(pk=pk)
        questions = []
        for i in quiz.get_question():
            answers = []
            for j in i.get_answers():
                answers.append(j.response)
            questions.append({str(i): answers})
        return JsonResponse({
            'data': questions,
            'time': quiz.time
        })


class save_quiz(View):
    def post(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=request.user.pk)
        form = get_object_or_404(Forms, pk=request.forms.pk)
        print(f'user:{user}'
              f'forms_id:{form}')
        redirect('homepage')
# * login


class Login(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('homepage')

# * register user


class Register(FormView):
    fields = '__all__'
    template_name = 'register.html'
    form_class = RegiterForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(Register, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('homepage')
        return super(Register, self).get(*args, **kwargs)

# * logaud


class Logaud(LogoutView):

    def get_success_url(self):
        return reverse_lazy('homepage')