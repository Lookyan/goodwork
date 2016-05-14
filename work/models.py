# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from managers import CompanyManager, JobTypeManager
from django.db import connection

User.__unicode__ = lambda self: self.email


class Profile(models.Model):
    user = models.OneToOneField(User)
    REGULAR_USER = 'RU'
    MODERATOR = 'MO'

    TYPE_OF_USER_CHOICES = (
        (REGULAR_USER, 'Regular User'),
        (MODERATOR, 'Moderator'),
    )
    group = models.CharField(max_length=2,
                             choices=TYPE_OF_USER_CHOICES,
                             default=REGULAR_USER)


class Company(models.Model):

    class Meta:
        verbose_name = 'Компания'
        verbose_name_plural = 'Компании'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200, verbose_name='Название')
    user = models.ForeignKey(User, null=True, blank=True, verbose_name='Пользователь')
    website = models.CharField(max_length=100, null=True, blank=True, verbose_name='Веб-сайт')
    logo = models.ImageField(upload_to='companies', default=None, null=True, blank=True, verbose_name='Логотип')

    EMP1_50 = '1'
    EMP51_200 = '2'
    EMP201_500 = '3'
    EMP501_1000 = '4'
    EMP1001_5000 = '5'
    EMPGT5000 = '6'
    UNKNOWN = '7'

    SIZE_EMPS_CHOICES = (
        (EMP1_50, '1-50'),
        (EMP51_200, '51-200'),
        (EMP201_500, '201-500'),
        (EMP501_1000, '501-1000'),
        (EMP1001_5000, '1001-5000'),
        (EMPGT5000, '> 5000'),
        (UNKNOWN, 'Неизвестно'),
    )
    size = models.CharField(max_length=1,
                            choices=SIZE_EMPS_CHOICES,
                            default=UNKNOWN,
                            verbose_name='Количество сотрудников')
    engaged = models.BooleanField(default=False, verbose_name='Подтвержден')
    founded = models.PositiveSmallIntegerField(default=0, blank=True, verbose_name='Основана')
    revenue = models.IntegerField(default=0, blank=True, verbose_name='Доход')
    description = models.TextField(blank=True, verbose_name='Описание')
    is_publicated = models.BooleanField(default=False, verbose_name='Опубликовано')
    is_deleted = models.BooleanField(default=False, verbose_name='Удалено')
    objects = CompanyManager()

    def get_pos_avg_salary(self):
        cursor = connection.cursor()
        cursor.execute('''SELECT c.name, j.name, AVG(s.value)
                          FROM work_salary s
                          JOIN work_jobtype j ON j.id = s.job_id
                          JOIN work_company c ON c.id = s.company_id
                          WHERE c.id = %s
                          GROUP BY j.id
                       ''', [self.id])
        return cursor.fetchall()

    def count_interview(self):
        cursor = connection.cursor()
        cursor.execute('''SELECT j.name, COUNT(i.id)
                                         FROM work_interview i
                                         JOIN work_jobtype j ON j.id = i.job_id
                                         JOIN work_company c ON c.id = i.company_id
                                         WHERE c.id = %s
                                         GROUP BY i.job_id
                                      ''', [self.id])
        return cursor.fetchall()


class Job(models.Model):

    class Meta:
        verbose_name = 'Вакансия'
        verbose_name_plural = 'Вакансии'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200, verbose_name='Название')
    company = models.ForeignKey('Company', verbose_name='Компания')
    description = models.TextField(verbose_name='Описание')
    date_added = models.DateField(auto_now_add=True, verbose_name='Добавлено')
    location = models.ForeignKey('City', default=None, null=True, blank=True, verbose_name='Город')
    experience = models.PositiveSmallIntegerField(default=0, verbose_name='Опыт')
    category = models.ForeignKey('Category', verbose_name='Категория')
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    INTERNSHIP = 'IS'
    TEMPORARY = 'TY'
    ENTRY_LEVEL = 'EL'
    NOT_CHECKED = 'NC'

    TYPE_OF_JOB_CHOICES = (
        (FULL_TIME, 'Полная занятость'),
        (PART_TIME, 'Частичная занятость'),
        (CONTRACT, 'Проектная работа'),
        (INTERNSHIP, 'Стажировка'),
        (TEMPORARY, 'Временная работа'),
        (ENTRY_LEVEL, 'Начало карьеры'),
        (NOT_CHECKED, 'Не выбрано'),
    )
    type = models.CharField(max_length=2,
                            choices=TYPE_OF_JOB_CHOICES,
                            default=FULL_TIME,
                            verbose_name='Тип')


class Category(models.Model):

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=200, verbose_name='Название')
    parent = models.ForeignKey('Category', default=None, null=True, blank=True, verbose_name='Родитель')
    icon = models.ImageField(upload_to='categories', default=None, null=True, blank=True, verbose_name='Иконка')


class City(models.Model):

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=50, verbose_name='Имя')


class Review(models.Model):

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __unicode__(self):
        return self.title

    user = models.ForeignKey(User, default=None, verbose_name='Пользователь')
    company = models.ForeignKey(Company, verbose_name='Компания')
    is_publicated = models.BooleanField(default=False, verbose_name='Опубликовано')

    R1 = 1
    R2 = 2
    R3 = 3
    R4 = 4
    R5 = 5
    RATING_CHOICES = (
        (R1, '1'),
        (R2, '2'),
        (R3, '3'),
        (R4, '4'),
        (R5, '5')
    )
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES,
                                              default=R5, verbose_name='Рейтинг')
    is_current_employee = models.BooleanField(default=False, verbose_name='Текущий сотрудник')
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    INTERN = 'IN'
    FREELANCE = 'FL'
    NOT_CHECKED = 'NC'

    EMPLOYMENT_STATUS = (
        (FULL_TIME, 'Полная занятость'),
        (PART_TIME, 'Частичная занятость'),
        (CONTRACT, 'Проектная работа'),
        (INTERN, 'Стажировка'),
        (FREELANCE, 'Удаленная работа'),
        (NOT_CHECKED, 'Не выбрано'),
    )
    status = models.CharField(max_length=2,
                              choices=EMPLOYMENT_STATUS,
                              default=NOT_CHECKED,
                              verbose_name='Статус')
    title = models.CharField(max_length=200, default=None, null=True, blank=True, verbose_name='Заголовок')
    pros = models.TextField(verbose_name='Преимущества')
    cons = models.TextField(verbose_name='Недостатки')

    def rating_range(self):
        return range(self.rating)


class Salary(models.Model):

    class Meta:
        verbose_name = 'Зарплата'
        verbose_name_plural = 'Зарплаты'

    def __unicode__(self):
        return self.company.name

    user = models.ForeignKey(User, default=None, verbose_name='Пользователь')
    job = models.ForeignKey('JobType', verbose_name='Позиция')
    company = models.ForeignKey('Company', verbose_name='Компания')
    value = models.IntegerField(default=0, verbose_name='Значение')

    LESS_YEAR = 0
    ONE_YEAR = 1
    TWO_YEARS = 2
    THREE_FIVE_YEARS = 3
    SIX_TEN_YEARS = 6
    MORE_TEN_YEARS = 10

    EXPERIENCE_CHOICES = (
        (LESS_YEAR, 'Меньше года'),
        (ONE_YEAR, 'Один год'),
        (TWO_YEARS, 'Два года'),
        (THREE_FIVE_YEARS, '3-5 лет'),
        (SIX_TEN_YEARS, '6-10 лет'),
        (MORE_TEN_YEARS, 'Больше 10 лет')
    )

    experience = models.PositiveSmallIntegerField(choices=EXPERIENCE_CHOICES,
                                                  default=LESS_YEAR,
                                                  verbose_name='Опыт')
    location = models.ForeignKey('City', default=None, null=True, blank=True, verbose_name='Город')
    FULL_TIME = 'FT'
    PART_TIME = 'PT'
    CONTRACT = 'CT'
    INTERN = 'IN'
    FREELANCE = 'FL'
    NOT_CHECKED = 'NC'

    EMPLOYMENT_STATUS = (
        (FULL_TIME, 'Полная занятость'),
        (PART_TIME, 'Частичная занятость'),
        (CONTRACT, 'Проектная работа'),
        (INTERN, 'Стажер'),
        (FREELANCE, 'Удаленная работа'),
        (NOT_CHECKED, 'Не выбрано'),
    )
    status = models.CharField(max_length=2,
                              choices=EMPLOYMENT_STATUS,
                              default=NOT_CHECKED,
                              verbose_name='Статус')

    @staticmethod
    def avg_salaries(comps):
        avg_salaries = {}
        cursor = connection.cursor()
        for comp in comps:
            cursor.execute('''SELECT c.name, j.name, AVG(s.value)
                                             FROM work_salary s
                                             JOIN work_jobtype j ON j.id = s.job_id
                                             JOIN work_company c ON c.id = s.company_id
                                             WHERE c.id = %s
                                             GROUP BY j.id
                                          ''', [comp.id])
            avg_salaries[comp.id] = cursor.fetchall()
        return avg_salaries


class JobType(models.Model):

    class Meta:
        verbose_name = 'Позиция'
        verbose_name_plural = 'Позиции'

    def __unicode__(self):
        return self.name

    name = models.CharField(max_length=250, verbose_name='Название')
    objects = JobTypeManager()


class Interview(models.Model):

    class Meta:
        verbose_name = 'Собеседование'
        verbose_name_plural = 'Собеседования'

    def __unicode__(self):
        return "'" + self.job.name + "' at " + self.company.name

    user = models.ForeignKey(User, default=None)
    POSITIVE = '+'
    NEGATIVE = '-'
    NEUTRAL = '?'

    TYPE_EXPERIENCE = (
        (POSITIVE, 'Позитивный'),
        (NEGATIVE, 'Негативный'),
        (NEUTRAL, 'Нейтральный')
    )
    experience = models.CharField(max_length=1,
                                  choices=TYPE_EXPERIENCE,
                                  default=POSITIVE,
                                  verbose_name='Опыт')
    job = models.ForeignKey('JobType', verbose_name='Позиция')
    description = models.TextField(verbose_name='Описание')
    question = models.ManyToManyField('InterviewQuestion', verbose_name='Вопросы')
    company = models.ForeignKey('Company', verbose_name='Компания')
    is_publicated = models.BooleanField(default=False, verbose_name='Опубликовано')
    VERY_EASY = 'VE'
    EASY = 'E'
    AVERAGE = 'A'
    DIFFICULT = 'D'
    VERY_DIFFICULT = 'VD'
    NOT_CHECKED = 'NC'

    TYPE_DIFFICULTY = (
        (VERY_EASY, 'Очень просто'),
        (EASY, 'Просто'),
        (AVERAGE, 'Средней сложности'),
        (DIFFICULT, 'Сложно'),
        (VERY_DIFFICULT, 'Очень сложно'),
        (NOT_CHECKED, 'Не выбрано'),
    )
    difficulty = models.CharField(max_length=2,
                                  choices=TYPE_DIFFICULTY,
                                  default=NOT_CHECKED,
                                  verbose_name='Сложность')
    YES = 'Y'
    DECLINED = 'D'
    NO = 'N'

    TYPE_OFFER = (
        (YES, 'Да'),
        (DECLINED, 'Да, но было отклонено'),
        (NO, 'Нет'),
        (NOT_CHECKED, 'Не выбрано'),
    )
    offer = models.CharField(max_length=1,
                             choices=TYPE_OFFER,
                             default=NOT_CHECKED,
                             verbose_name='Предложение')
    entire_process = models.PositiveSmallIntegerField(default=0, verbose_name='Весь процесс занял')
    DAYS = 'D'
    WEEKS = 'W'
    MONTHS = 'M'

    DURATION_IN = (
        (DAYS, 'Дней'),
        (WEEKS, 'Недель'),
        (MONTHS, 'Месяцев'),
    )
    duration = models.CharField(max_length=1,
                                choices=DURATION_IN,
                                default=DAYS,
                                verbose_name='Продолжительность')
    place = models.CharField(max_length=250, verbose_name='Место проведения')


class InterviewQuestion(models.Model):

    class Meta:
        verbose_name = 'Вопрос на интервью'
        verbose_name_plural = 'Вопросы на интервью'

    def __unicode__(self):
        return self.question

    question = models.TextField(verbose_name='Вопрос')
    answer = models.TextField(verbose_name='Ответ')

    @staticmethod
    def add_questions(questions, answers):
        if not questions or not answers or len(questions) != len(answers):
            return []
        qids = []
        for question in zip(questions, answers):
            q = InterviewQuestion(question=question[0], answer=question[1])
            q.save()
            qids.append(q)
        return qids