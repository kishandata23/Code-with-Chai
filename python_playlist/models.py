from django.db import models

# Create your models here.
class Python_Video(models.Model):
    name = models.CharField(max_length=100, null=False)
    link = models.CharField(max_length=500, null=False)

    def __str__(self) -> str:
        return self.name