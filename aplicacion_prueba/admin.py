from django.contrib import admin
from .models import Profile, Question, Answers, Forms, Resuls


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'total_score',)


class AnswerseAdmin(admin.TabularInline):
    model = Answers
    can_delete = False
    max_num = Answers.max_response
    min_num = Answers.min_response


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    inlines = (AnswerseAdmin,)
    list_display = ('question',)
    search_fields = ('question', 'response_question__correct')


@admin.register(Forms)
class FormAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title', 'forms_question__question',)


admin.site.register(Resuls)
admin.site.register(Answers)
