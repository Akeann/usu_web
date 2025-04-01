from django.db import models
from users.models import User

class Request(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'request in progress'),
        ('completed', 'request completed'),
    ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='in_progress')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    result_path = models.CharField(max_length=255, null=True, blank=True)
    sent_at = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='requests')

    def __str__(self):
        return f"Request {self.id} by {self.user.email}"

class PipelineParams(models.Model):
    PIPELINE_TYPE_CHOICES = [
        ('nanopore', 'Nanopore'),
        ('illumina', 'Illumina'),
    ]

    pipeline_type = models.CharField(max_length=20, choices=PIPELINE_TYPE_CHOICES)
    data_arch_path = models.CharField(max_length=255)
    adapter = models.CharField(max_length=255, null=True, blank=True)
    classifier = models.CharField(max_length=255, null=True, blank=True)
    ref_seq = models.CharField(max_length=255)
    ref_database = models.CharField(max_length=255)
    minlen = models.IntegerField(default=150)
    maxns = models.IntegerField(default=5)
    maxee = models.FloatField(default=2.0)
    min_quality = models.IntegerField(default=20)
    max_ambiguous = models.IntegerField(default=2)
    trim_left = models.IntegerField(default=80)
    trim_right = models.IntegerField(default=700)
    request = models.OneToOneField(Request, on_delete=models.CASCADE, related_name='pipeline_params')

    def __str__(self):
        return f"PipelineParams for {self.request.id}"