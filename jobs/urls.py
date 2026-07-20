from django.urls import path
from .views import job_list, create_job, edit_job, close_job, open_job, closed_jobs, delete_job

urlpatterns = [
    path(
        '',
        job_list,
        name='job-list'
    ),

    path(
        'jobs/create/',
        create_job,
        name='create-job'
    ),

    path(
        'jobs/edit/<int:job_id>/',
        edit_job,
        name='edit-job'
    ),

    path(
        'jobs/close/<int:job_id>/',
        close_job,
        name='close-job'
    ),
    
    
    path(
        'jobs/open/<int:job_id>/',
        open_job,
        name='open-job'
    ),
    
    path(
        'jobs/closed/',
        closed_jobs,
        name='closed-jobs'
),
    path(
        'jobs/delete/<int:job_id>/',
        delete_job,
        name='delete-job'
    )
]


