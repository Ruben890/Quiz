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

from .models import Profile, Question, Answers, QUiz, Resuls

from django.core.paginator import Paginator


class Homepage(View):

    def get(self, request, *args, **kwargs):

        return render(request, 'index.html', {'form': QUiz.objects.all(),

                                              'user': Profile.objects.all()})


class Quiz(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):

        quiz = QUiz.objects.get(pk=pk)

        return render(request, 'Quiz.html', {'quiz': quiz})


class quiz_view(LoginRequiredMixin, View):

    def get(self, request, pk, *args, **kwargs):

        quiz = QUiz.objects.get(pk=pk)

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


class save_quiz(LoginRequiredMixin, View):

    def post(self, request, pk, *args, **kwargs):

        data = request.POST

        questions = []
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Question.objects.get(question=k)
            questions.append(question)

        user = request.user
        quiz = QUiz.objects.get(pk=pk)
        score: int = 0
        result = []
        corect_answer = None
        for q in questions:

            a_select = request.POST.get(q.question)

            if a_select != "":
                questions_answer = Answers.objects.filter(question=q)
                for a in questions_answer:
                    if a_select == a.response:
                        if a.correct:
                            score += 1
                            corect_answer = a.response
                        else:
                            if a.correct:
                                corect_answer = a.response
                result.append(

                    {str(q): {'corect_answer': corect_answer, 'answers': a_select}})
            else:

                result.append({str(q): 'not answers'})

        _score = score * 100 / quiz.number_of_questions

        if _score >= quiz.total_score_question:

            Resuls.objects.create(quiz=quiz, user=user,
                                  score=_score, complete=True)
            return JsonResponse({'passed': True, 'score': _score, 'Resuls': result})
        else:

            Resuls.objects.create(quiz=quiz, user=user,
                                  score=_score, complete=False)
            return JsonResponse({

                'Passed': False,
                'score': _score,
                'Resuls': result

            })

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
