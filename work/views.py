# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect
from django.http import HttpResponseBadRequest, JsonResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from goodwork.forms import SignUpForm, CompanyAddForm, ReviewAddForm, SalaryAddForm, InterviewAddForm
from django.contrib.auth.decorators import login_required
from work.models import Company, JobType, Salary, InterviewQuestion
from django.contrib.auth import update_session_auth_hash

PER_PAGE = 10


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
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return render(request, 'settings.html', {'done': True, 'form': form})
    else:
        form = PasswordChangeForm(request.user)

    return render(request, 'settings.html', {'form': form})


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
        # create interview questions
        qids = InterviewQuestion.add_questions(request.POST.getlist('question'), request.POST.getlist('answer'))
        form = InterviewAddForm(request.POST)
        if form.is_valid():
            job_name = request.POST.get('job_name')
            if job_name is None or job_name == '':
                return redirect('/add')
            job_type = JobType.objects.create_if_not_exist(job_name)
            interview = form.save(commit=False)
            interview.user = request.user
            interview.job = job_type
            interview.company = Company.objects.get(name__iexact=company)
            interview.save()
            map(interview.question.add, qids)
            return render(request, 'info-added.html', {})

    return render(request, 'add-interview.html', {'company': company, 'form': form})


def companies(request):
    company = request.GET.get('q')
    if company is None:
        return redirect('/')
    comps = Company.objects.filter(name__icontains=company, is_publicated=True)[:PER_PAGE]
    return render(request, 'search-company.html', {'companies': comps, 'q': company, 'url': 'company'})


def interviews(request):
    company = request.GET.get('q')
    if company is None:
        return redirect('/')
    comps = Company.objects.filter(name__icontains=company, is_publicated=True)

    return render(request, 'search-interview.html', {'companies': comps, 'q': company, 'url': 'interview'})


def salaries(request):
    company = request.GET.get('q')
    if company is None:
        return redirect('/')
    comps = Company.objects.filter(name__icontains=company, is_publicated=True)

    # aggregate salaries by positions
    avg_salaries = Salary.avg_salaries(comps)
    return render(request, 'search-salary.html',
                  {'companies': comps, 'q': company, 'avg_sals': avg_salaries, 'url': 'salary'})


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


def get_data(request):
    url = request.GET.get('url')
    try:
        company = str(request.GET.get('company'))
        page = int(request.GET.get('page'))
    except ValueError:
        return HttpResponseBadRequest()
    if not url or not page:
        return HttpResponseBadRequest()
    offset = (page - 1) * PER_PAGE
    limit = PER_PAGE
    if url == 'company':
        comps = Company.objects.filter(name__icontains=company, is_publicated=True)[offset:offset + limit]
        return render(request, 'company-entities.html', {'companies': comps})
    if url == 'salary':
        comps = Company.objects.filter(name__icontains=company, is_publicated=True)[offset:offset + limit]
        avg_salaries = Salary.avg_salaries(comps)
        return render(request, 'salary-entities.html', {'companies': comps, 'q': company, 'avg_sals': avg_salaries})
    # interview soon