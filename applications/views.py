from email.mime import application

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.models import Job
from .models import Application
from django.shortcuts import render
from jobs.models import Job
from django.db.models import Count
from django.core.files.storage import default_storage



@login_required
def apply_job(request, job_id):

    job = get_object_or_404(
        Job,
        id=job_id
    )

    profile = request.user.userprofile

    if profile.role != "candidate":
        messages.error(
            request,
            "HR cannot apply for jobs."
        )
        return redirect("/")

    exists = Application.objects.filter(
        candidate=request.user,
        job=job
    ).exists()

    if exists:
        messages.info(
            request,
            "You already applied this job."
        )
        return redirect("/")

    if request.method == "POST":

        cv = request.FILES.get("cv_file")

        Application.objects.create(
            candidate=request.user,
            job=job,
            cv_file=cv
        )

        messages.success(
            request,
            "Apply successfully!"
        )

        return redirect("/")

    return render(
        request,
        "applications/apply_job.html",
        {
            "job": job
        }
    )




@login_required
def my_applications(request):

    applications = Application.objects.filter(
        candidate=request.user
    )

    return render(
        request,
        'applications/my_applications.html',
        {
            'applications': applications
        }
    )
    
    
@login_required
def manage_applications(
    request,
    job_id
):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can access this page."
        )
        return redirect('/')

    job = get_object_or_404(
        Job,
        id=job_id
    )

    applications = Application.objects.filter(
        job=job
    )

    return render(
        request,
        "applications/manage_applications.html",
        {
            "applications": applications,
            "job": job
        }
    )


@login_required
def update_application_status(
    request,
    application_id,
    new_status
    ):
    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can update status."
        )
        return redirect('/')

    application = get_object_or_404(
        Application,
        id=application_id
    )

    # Nếu HR accept
    if new_status == 'accepted':

        application.status = 'accepted'
        application.save()

        # Reject tất cả application khác
        Application.objects.filter(
            candidate=application.candidate
        ).exclude(
            id=application.id
        ).update(
            status='rejected'
        )

        messages.success(
            request,
            "Candidate accepted. Other applications rejected."
        )

    else:

        application.status = new_status
        application.save()

        messages.success(
            request,
            "Status updated successfully."
        )

    return redirect(
        f'/applications/manage/{application.job.id}/'
    )

@login_required
def cancel_application(
    request,
    application_id
):

    application = get_object_or_404(
        Application,
        id=application_id,
        candidate=request.user
    )

    if application.status != 'pending':
        messages.error(
            request,
            "Only pending applications can be cancelled."
        )
        return redirect('/applications/my-applications/')

    application.delete()

    messages.success(
        request,
        "Application cancelled."
    )

    return redirect('/applications/my-applications/')


@login_required
def hr_dashboard(request):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can access dashboard."
        )
        return redirect('/')

    context = {

        "total_jobs": Job.objects.count(),

        "open_jobs": Job.objects.filter(
            status="open"
        ).count(),

        "closed_jobs": Job.objects.filter(
            status="closed"
        ).count(),

        "total_applications": Application.objects.count(),

        "pending": Application.objects.filter(
            status="pending"
        ).count(),

        "reviewing": Application.objects.filter(
            status="reviewing"
        ).count(),

        "interview": Application.objects.filter(
            status="interview"
        ).count(),

        "accepted": Application.objects.filter(
            status="accepted"
        ).count(),

        "rejected": Application.objects.filter(
            status="rejected"
        ).count(),

    }

    return render(
        request,
        "applications/hr_dashboard.html",
        context
    )
    
    
@login_required
def manage_jobs(request):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can access."
        )
        return redirect('/')

    jobs = Job.objects.annotate(
        applicant_count=Count('application')
    )

    return render(
        request,
        "applications/manage_jobs.html",
        {
            "jobs": jobs
        }
    )
    
@login_required
def update_cv(
    request,
    application_id
):

    application = get_object_or_404(
        Application,
        id=application_id,
        candidate=request.user
    )

    if request.method == "POST":

        if "cv_file" in request.FILES:

            if application.cv_file:
                application.cv_file.delete()

            application.cv_file = request.FILES["cv_file"]

            application.save()

            messages.success(
                request,
                "CV updated successfully."
            )

            return redirect(
                "/applications/my-applications/"
            )

    return render(
        request,
        "applications/update_cv.html",
        {
            "application": application
        }
    )