# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from goodwork.forms import SignUpForm, CompanyAddForm, ReviewAddForm, SalaryAddForm, InterviewAddForm
from django.contrib.auth.decorators import login_required
from work.models import Company, JobType, Salary
from django.db import connection


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
            job_name = request.POST.get('job_name')
            if job_name is None or job_name == '':
                return redirect('/add')
            job_type = JobType.objects.create_if_not_exist(job_name)
            salary = form.save(commit=False)
            salary.user = request.user
            salary.job = job_type
            salary.company = Company.objects.get(name__iexact=company)
            salary.save()
            return render(request, 'info-added.html', {})
    return render(request, 'add-salary.html', {'company': company, 'form': form})


@login_required
def add_interview(request):
    company = request.GET.get("company")
    if company is None:
        return redirect('/add')
    if not Company.objects.check_company_exists(company):
        return redirect('/add')
    if request.method == 'GET':
        form = InterviewAddForm()
    else:
        form = InterviewAddForm(request.POST)
    return render(request, 'add-interview.html', {'company': company, 'form': form})


def companies(request):
    company = request.GET.get('q')
    if company is None:
        return redirect('/')
    comps = Company.objects.filter(name__icontains=company)
    return render(request, 'search-company.html', {'companies': comps, 'q': company})


def interviews(request):
    pass


def salaries(request):
    company = request.GET.get('q')
    if company is None:
        return redirect('/')
    comps = Company.objects.filter(name__icontains=company)

    # aggregate salaries by positions
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
    return render(request, 'search-salary.html', {'companies': comps, 'q': company, 'avg_sals': avg_salaries})


def companyjs(request):
    term = request.GET.get('term')
    if term is None:
        return HttpResponseBadRequest()
    if len(term) < 3:
        return HttpResponseBadRequest()
    data = Company.objects.get_by_name_part(term)
    return JsonResponse(data, safe=False)


def position_js(request):
    position = request.GET.get('term')
    if position is None:
        return HttpResponseBadRequest()
    if len(position) < 3:
        return HttpResponseBadRequest()
    data = JobType.objects.get_by_title_part(position)
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