from django.urls import path
from .views import apply_job, manage_jobs, my_applications, manage_applications, update_application_status, cancel_application, hr_dashboard, manage_applications, update_cv

urlpatterns = [
    path('apply/<int:job_id>/', apply_job, name='apply-job'),

    path(
        'my-applications/',
        my_applications,
        name='my-applications'
    ),
    
    
    path(
        "manage/<int:job_id>/",
        manage_applications,
        name="manage-applications"
    ),
    
    path(
        'update-status/<int:application_id>/<str:new_status>/',
        update_application_status,
        name='update-status'
    ),
    
    path(
        'cancel/<int:application_id>/',
        cancel_application,
        name='cancel-application'
),
    
    path(
        'hr-dashboard/',
        hr_dashboard,
        name='hr-dashboard'
    ),
    
    
    path(
        "manage-jobs/",
        manage_jobs,
        name="manage-jobs"
),
    
    path(
        "update-cv/<int:application_id>/",
        update_cv,
        name="update-cv"
    ),
]