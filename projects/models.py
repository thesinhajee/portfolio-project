from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=50, null=True)
    image=models.ImageField(upload_to='images/')
    summary=models.CharField(max_length=150)

    def __str__(self):
        return self.title
