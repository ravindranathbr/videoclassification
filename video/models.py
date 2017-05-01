from django.db import models

# Create your models here.

class Video(models.Model):
    url = models.CharField(max_length=256, null=True)
    downloadStatus = models.CharField(max_length=50, null=True)
    processingStatus = models.CharField(max_length=50, null=True)
    # <process1, process2, ... >
    typeOfProcesses = models.TextField(null=True)
    # <processType:value>
    testResult = models.TextField(null=True)
    created_at = models.DateTimeField('date_published', null=True)
    lastProcessed = models.DateTimeField('date_published', null=True)

