from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import Job



def job_list(request):

    jobs = Job.objects.filter(
        status='open'
    )

    keyword = request.GET.get(
        'keyword',
        ''
    )

    location = request.GET.get(
        'location',
        ''
    )

    if keyword:

        jobs = jobs.filter(
            title__icontains=keyword
        )

    if location:

        jobs = jobs.filter(
            location__icontains=location
        )

    return render(
        request,
        'jobs/job_list.html',
        {
            'jobs': jobs,
            'keyword': keyword,
            'location': location
        }
    )

@login_required
def create_job(request):

    profile = request.user.userprofile

    if profile.role != 'hr':

        messages.error(
            request,
            "Only HR can create jobs."
        )

        return redirect('/')

    if request.method == 'POST':

        Job.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            requirements=request.POST.get('requirements'),
            location=request.POST.get('location'),
            salary=request.POST.get('salary'),
            created_by=request.user
        )

        messages.success(
            request,
            "Job created successfully."
        )

        return redirect('/')

    return render(
        request,
        'jobs/create_job.html'
    )

@login_required
def edit_job(request, job_id):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can edit jobs."
        )
        return redirect('/')

    job = get_object_or_404(
        Job,
        id=job_id
    )

    if request.method == 'POST':

        job.title = request.POST.get('title')
        job.description = request.POST.get('description')
        job.requirements = request.POST.get('requirements')
        job.location = request.POST.get('location')
        job.salary = request.POST.get('salary')

        job.save()

        messages.success(
            request,
            "Job updated successfully."
        )

        return redirect('/')

    return render(
        request,
        'jobs/edit_job.html',
        {
            'job': job
        }
    )



@login_required
def close_job(request, job_id):
    
    profile = request.user.userprofile
    
    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can close jobs."
        )
        return redirect('/')
    
    job = get_object_or_404(
        Job,
        id=job_id
    )
    
    job.status = 'closed'
    job.save()
    
    messages.success(
        request,
        "Job closed successfully."
    )
    
    return redirect('/')


@login_required
def open_job(request, job_id):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can open jobs."
        )
        return redirect('/')

    job = get_object_or_404(
        Job,
        id=job_id
    )

    job.status = 'open'
    job.save()

    messages.success(
        request,
        "Job reopened successfully."
    )

    return redirect('/')



@login_required
def closed_jobs(request):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can access."
        )
        return redirect('/')

    jobs = Job.objects.filter(
        status='closed'
    )

    return render(
        request,
        'jobs/closed_jobs.html',
        {
            'jobs': jobs
        }
    )
    
    
    
@login_required
def delete_job(request, job_id):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can delete jobs."
        )
        return redirect('/')

    job = get_object_or_404(
        Job,
        id=job_id
    )

    job.delete()

    messages.success(
        request,
        "Job deleted permanently."
    )

    return redirect('/jobs/closed/')