from django.db import models
from applications.models import Application

class Interview(models.Model):

    application = models.OneToOneField(
        Application,
        on_delete=models.CASCADE
    )
    
    interview_time = models.DateTimeField()
    
    location = models.CharField(
        max_length=200
    )
    
    note = models.TextField(
        blank=True
    )
    
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    
    def __str__(self):
        return (
            f"{self.application.candidate.username}"
            f" - "
            f"{self.application.job.title}"
        )

