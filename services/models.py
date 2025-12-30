from django.db import models
from Elischama.settings import AUTH_USER_MODEL

# Create your models here.
class Service(models.Model):
    STATUS = (
        ('pending', 'Pendiente'),
        ('progress', 'En proceso'),
        ('done', 'Terminado'),
    )

    client = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    source_language = models.CharField(max_length=50)
    target_language = models.CharField(max_length=50)
    document = models.FileField(upload_to='documents/')
    translated_file = models.FileField(upload_to='translated/', null=True, blank=True)
    progress = models.IntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS)
    paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def can_download(self):
            return self.status == 'done' and self.paid

    def __str__(self):
        return f"Service - {self.client.username}"