# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from goodwork.forms import SignUpForm, CompanyAddForm, ReviewAddForm, SalaryAddForm
from django.contrib.auth.decorators import login_required
from work.models import Company


def home(request):
    return render(request, 'main.html', {})


def jobs(request):
    return render(request, 'jobs.html', {})


def job(request, job_id):
    return render(request, 'job.html', {})


def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'signin.html', {'error': '2'})
        else:
            return render(request, 'signin.html', {'error': '1'})
    else:
        return render(request, 'signin.html', {})


def signup(request):
    if request.method == 'POST':
        data = request.POST.copy()
        data['username'] = str(int(User.objects.latest('id').id) + 1)  # race condition!
        form = SignUpForm(data)
        if form.is_valid():
            user = form.save()
            return render(request, 'main.html', {})
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required
def settings(request):
    return render(request, 'settings.html', {})


@login_required
def add(request):
    if request.method == 'GET':
        company_add_form = CompanyAddForm()
        return render(request, 'add.html', {'form': company_add_form})


@login_required
def add_review(request):
    company = request.GET.get("company")
    if company is None:
        return redirect('/add')
    if not Company.objects.check_company_exists(company):
        return redirect('/add')
    if request.method == 'GET':
        form = ReviewAddForm()
    else:
        form = ReviewAddForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.company = Company.objects.get(name__iexact=company)
            review.user = request.user
            review.save()
            return render(request, 'info-added.html', {})
    return render(request, 'add-review.html', {'form': form, 'company': company})


@login_required
def add_salary(request):
    company = request.GET.get("company")
    if company is None:
        return redirect('/add')
    if not Company.objects.check_company_exists(company):
        return redirect('/add')
    if request.method == 'GET':
        form = SalaryAddForm()
    else:
        form = SalaryAddForm(request.POST)
        if form.is_valid():
            return render(request, 'info-added.html', {})
    return render(request, 'add-salary.html', {'company': company, 'form': form})


@login_required
def add_interview(request):
    pass


def companies(request):
    pass


def interviews(request):
    pass


def salaries(request):
    pass


def companyjs(request):
    term = request.GET.get('term')
    if term is None:
        return HttpResponseBadRequest()
    if len(term) < 3:
        return HttpResponseBadRequest()
    data = Company.objects.get_by_name_part(term)
    return JsonResponse(data, safe=False)


def company_check(request):
    name = request.GET.get('name')
    if name is None:
        return HttpResponseBadRequest
    if Company.objects.check_company_exists(name):
        return JsonResponse({'result': True})
    else:
        return JsonResponse({'result': False})


@login_required
def company_create_js(request):
    form = CompanyAddForm(request.POST)
    if form.is_valid():
        company = form.save(commit=False)
        company.name = request.POST.get("name")
        company.save()
        return JsonResponse({'result': 'ok'})
    else:
        return JsonResponse({'result': 'error'})