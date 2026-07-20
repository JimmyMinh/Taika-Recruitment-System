from django.db import models
from django.contrib.auth.models import User
from jobs.models import Job


class Application(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('reviewing', 'Reviewing'),
        ('interview', 'Interview'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected'),
    ]

    candidate = models.ForeignKey(User, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    cv_file = models.FileField(upload_to='cv/')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    applied_at = models.DateTimeField(auto_now_add=True)

    reviewed_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        unique_together = ('candidate', 'job')

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"