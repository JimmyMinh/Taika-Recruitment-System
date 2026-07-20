from django.urls import path
from .views import (
    schedule_interview,
    my_interviews
)

urlpatterns = [

    path(
        'schedule/<int:application_id>/',
        schedule_interview,
        name='schedule-interview'
    ),

    path(
        'my-interviews/',
        my_interviews,
        name='my-interviews'
    ),
]