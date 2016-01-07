from django.shortcuts import render


def home(request):
    return render(request, 'main.html', {})


def jobs(request):
    return render(request, 'jobs.html', {})


def job(request, job_id):
    return render(request, 'job.html', {})