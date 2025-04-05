from django.db import models
from users.models import User  # Импортируем кастомную модель User

class Request(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'Request in progress'),
        ('completed', 'Request completed'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_progress',
        verbose_name='Status'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Created at'
    )
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Deleted at'
    )
    result_path = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Result path'
    )
    sent_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name='Sent at'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='requests',
        verbose_name='User'
    )

    class Meta:
        verbose_name = 'Request'
        verbose_name_plural = 'Requests'
        ordering = ['-created_at']

    def __str__(self):
        return f"Request {self.id} by {self.user.email}"


class PipelineParams(models.Model):
    PIPELINE_TYPE_CHOICES = [
        ('nanopore', 'Nanopore'),
        ('illumina', 'Illumina'),
    ]

    pipeline_type = models.CharField(
        max_length=20,
        choices=PIPELINE_TYPE_CHOICES,
        verbose_name='Pipeline type'
    )
    data_arch_path = models.CharField(
        max_length=255,
        verbose_name='Data archive path'
    )
    adapter = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Adapter'
    )
    classifier = models.CharField(
        max_length=255,
        null=True,
        blank=True,
        verbose_name='Classifier'
    )
    ref_seq = models.CharField(
        max_length=255,
        verbose_name='Reference sequence'
    )
    ref_database = models.CharField(
        max_length=255,
        verbose_name='Reference database'
    )
    minlen = models.IntegerField(
        default=150,
        verbose_name='Minimum length'
    )
    maxns = models.IntegerField(
        default=5,
        verbose_name='Maximum Ns'
    )
    maxee = models.FloatField(
        default=2.0,
        verbose_name='Maximum expected errors'
    )
    min_quality = models.IntegerField(
        default=20,
        verbose_name='Minimum quality'
    )
    max_ambiguous = models.IntegerField(
        default=2,
        verbose_name='Maximum ambiguous bases'
    )
    trim_left = models.IntegerField(
        default=80,
        verbose_name='Trim left'
    )
    trim_right = models.IntegerField(
        default=700,
        verbose_name='Trim right'
    )
    request = models.OneToOneField(
        Request,
        on_delete=models.CASCADE,
        related_name='pipeline_params',
        verbose_name='Request'
    )

    class Meta:
        verbose_name = 'Pipeline Parameters'
        verbose_name_plural = 'Pipeline Parameters'

    def __str__(self):
        return f"PipelineParams for Request {self.request.id}"