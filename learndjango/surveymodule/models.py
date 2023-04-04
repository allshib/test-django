from django.db import models
from django.utils.translation import gettext_lazy as _


class Survey(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.CharField('Описание', max_length=250)
    createdate = models.DateTimeField('Дата создания')
    is_active = models.BooleanField('Ативен')

    def __str__(self):
        return f'{self.title}; Активен: {self.is_active}'


class Question(models.Model):
    class QuestionType(models.IntegerChoices):
        Choice = 0, _('Выбор')
        Date = 1, _('Дата')
        Text = 2, _('Текст')

    title = models.CharField('Текст вопроса', max_length=250)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    type_of_question = models.IntegerField(
        choices=QuestionType.choices,
        default=QuestionType.Choice)

    def __str__(self):
        return f'Тип: {self.type_of_question}; Вопрос:{self.title}'


class Answer(models.Model):
    class AnswerType(models.IntegerChoices):
        IsNull = 0, _('Пусто')
        String = 1, _('Строка')
        Integer = 2, _('Число')
        DateTime = 3, _('Дата')

    num = models.IntegerField('Номер ответа')
    text = models.CharField('Текст текст', max_length=250)
    related_value = models.CharField('Связанное значение', max_length=250)

    type_of_related_value = models.IntegerField(
        choices=AnswerType.choices,
        default=AnswerType.IsNull)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
