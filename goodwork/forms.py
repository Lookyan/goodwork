# -*- coding: utf-8 -*-

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from work.models import Profile, Company, Review, Salary
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    """ Require email address when a user signs up """
    email = forms.EmailField(label='Email', max_length=75)

    class Meta:
        model = User
        fields = ('username', 'email',)

    def clean_email(self):
        email = self.cleaned_data["email"]
        try:
            user = User.objects.get(email=email)
            raise forms.ValidationError("Такой email адрес уже зарегистрирован. Вы забыли пароль?")
        except User.DoesNotExist:
            return email

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.email = self.cleaned_data["email"]
        user.is_active = True    # change to false if using email activation
        if commit:
            user.save()
        profile = Profile()
        profile.group = Profile.REGULAR_USER
        profile.user = user
        profile.save()

        return user


class CompanyAddForm(ModelForm):
    class Meta:
        model = Company
        fields = ['website', 'size']
        labels = {
            'website': 'Веб-сайт',
            'size': 'Общее количество сотрудников'
        }
        widgets = {
            'website': forms.TextInput(attrs={'value': 'http://'})
        }


class ReviewAddForm(ModelForm):

    class Meta:
        model = Review
        fields = ['rating', 'is_current_employee', 'status', 'title', 'pros', 'cons']
        labels = {
            'rating': 'Оцените работу в компании',
            'is_current_employee': 'Вы являетесь действующим сотрудником?',
            'status': 'Тип занятости',
            'title': 'Заголовок отзыва',
            'pros': 'Преимущества работы в компании',
            'cons': 'Недостатки работы в компании'
        }
        widgets = {
            'pros': forms.Textarea(attrs={'class': 'materialize-textarea'}),
            'cons': forms.Textarea(attrs={'class': 'materialize-textarea'})
        }


class SalaryAddForm(ModelForm):
    job_name = forms.CharField(label='Должность')

    class Meta:
        model = Salary
        fields = ['job_name', 'value', 'experience', 'status']
        labels = {
            'value': 'Уровень заработной платы',
            'experience': 'Опыт работы',
            'status': 'Статус'
        }
        widgets = {
            'value': forms.NumberInput(attrs={'type': 'range', 'min': '10', 'max': '1000', 'class': 'salary-range'})
        }