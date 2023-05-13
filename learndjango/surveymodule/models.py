from django.db import models
from django.utils.translation import gettext_lazy as _


class Survey(models.Model):
    title = models.CharField('Название', max_length=250)
    description = models.CharField('Описание', max_length=250)
    createdate = models.DateTimeField('Дата создания')
    is_active = models.BooleanField('Ативен')

    def __str__(self):
        return f'{self.title}; Активен: {self.is_active}'


class BinaryChoice(models.Model):
    false_text = models.CharField('Текст отрицательного значения', max_length=100)
    true_text = models.CharField('Текст положительного значения', max_length=100)

    false_value = models.CharField('Связанное значение для False', max_length=20)
    true_value = models.CharField('Связанное значение для True', max_length=20)

    def __str__(self):
        return f'Бинарное значение: {self.false_text} и {self.true_text}'


class Question(models.Model):
    class QuestionType(models.IntegerChoices):
        Choice = 0, _('Выбор')
        Date = 1, _('Дата')
        Text = 2, _('Текст')
        Binary = 3, _('Бинарный')

    title = models.CharField('Текст вопроса', max_length=250)
    num = models.IntegerField('Порядковый номер вопроса')
    json_arr_index = models.IntegerField('Индекс в массиве', null=True, default=None, blank=True)
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)
    type_of_question = models.IntegerField(
        choices=QuestionType.choices,
        default=QuestionType.Choice)

    binary_value = models.ForeignKey(BinaryChoice, on_delete=models.CASCADE, null=True, default=None, blank=True)

    def __str__(self):
        return f'Тип: {self.type_of_question}; Вопрос:{self.title}'


class Answer(models.Model):
    class AnswerType(models.IntegerChoices):
        IsNull = 0, _('Пусто')
        String = 1, _('Строка')
        Integer = 2, _('Число')
        DateTime = 3, _('Дата')

    num = models.IntegerField('Номер ответа')
    text = models.CharField('Текст Ответа', max_length=250)
    related_value = models.CharField('Связанное значение', max_length=250)

    type_of_related_value = models.IntegerField(
        choices=AnswerType.choices,
        default=AnswerType.IsNull)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
