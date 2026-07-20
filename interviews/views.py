from email.mime import application

from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from applications.models import Application
from .models import Interview
from django.shortcuts import render
from datetime import datetime

@login_required
def schedule_interview(request, application_id):

    profile = request.user.userprofile

    if profile.role != 'hr':
        messages.error(
            request,
            "Only HR can schedule interviews."
        )
        return redirect('/')

    application = get_object_or_404(
        Application,
        id=application_id
    )
    
    try:
        interview = Interview.objects.get(
            application=application
        )
    except Interview.DoesNotExist:
        interview = Interview(
            application=application
        )

    if request.method == "POST":

        interview.interview_time = request.POST.get(
            "interview_time"
        )

        interview.location = request.POST.get(
            "location"
        )

        interview.note = request.POST.get(
            "note"
        )

        interview.save()

        messages.success(
            request,
            "Interview saved successfully."
        )

        return redirect(
            f'/applications/manage/{application.job.id}/'
        )

    return render(
        request,
        "interviews/schedule_interview.html",
        {
            "application": application,
            "interview": interview
        }
    )

@login_required
def my_interviews(request):

    interviews = Interview.objects.filter(
        application__candidate=request.user
    )

    return render(
        request,
        "interviews/my_interviews.html",
        {
            "interviews": interviews
        }
    )