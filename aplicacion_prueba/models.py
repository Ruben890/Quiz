from django.db import models
from django.contrib.auth.models import User
from .choices import puntos, nivel
import random


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name='Profile', unique=True)
    imagen = models.ImageField(
        default='questions.png', verbose_name='imagen_profile')
    total_score = models.IntegerField(default=0, verbose_name='total_score')

    def __str__(self):
        return self.user.username


class QUiz(models.Model):
    title = models.CharField('title', max_length=250,
                             null=False, blank=False, unique=True)
    author = models.ForeignKey(
        User, verbose_name="users_autho", on_delete=models.CASCADE, null=True, blank=True)
    imagen = models.ImageField(upload_to='forms', null=True, blank=True)
    create = models.TimeField(auto_now_add=True)
    time = models.IntegerField(
        default=0, verbose_name='time', help_text='Time to')
    descriction = models.TextField(
        verbose_name='descriction', blank=False, null=False)
    nivel = models.CharField(choices=nivel, max_length=10,
                             verbose_name='nivel', null=False, blank=False)
    total_score_question = models.IntegerField(
        default=0, verbose_name="required points", blank=False, null=False)
    number_of_questions = models.IntegerField(
        default=0, blank=False, null=False, verbose_name="number of questions")

    def __str__(self):
        return f'{self.title}'

    def get_question(self):
        questions = list(self.forms_question.all())
        random.shuffle(questions)
        return questions


class Question(models.Model):
    form = models.ForeignKey(
        'QUiz', on_delete=models.CASCADE, related_name='forms_question')
    user = models.ForeignKey(User, verbose_name="user_question",
                             on_delete=models.CASCADE, null=True, blank=True)
    question = models.TextField(
        verbose_name='question', null=False, blank=False)

    def __str__(self):
        return self.question

    def get_answers(self):
        return self.answers_question.all()

    class Meta:
        verbose_name = 'question'
        verbose_name_plural = 'questions'


class Answers(models.Model):
    max_response = 4
    min_response = 2
    question = models.ForeignKey(
        Question, related_name='answers_question', on_delete=models.CASCADE, null=False, blank=False)
    response = models.TextField(verbose_name='answers', null=True, blank=True)
    correct = models.BooleanField(default=False, null=False)

    def __str__(self):
        return self.response

    class Meta:
        verbose_name = 'answers'


class Resuls(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='Resuls_users')
    quiz = models.ForeignKey(
        QUiz, on_delete=models.CASCADE, related_name='Resuls', null=False, blank=False)
    score = models.FloatField(default=0, null=True, blank=False)
    complete = models.BooleanField(
        default=False, verbose_name="complete", null=False, blank=False)

    def __str__(self) -> str:
        return f'user:{self.user} quiz:{self.quiz}'
