from django.db import models

# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    date=models.DateTimeField(null=True)
    image=models.ImageField(upload_to='images/')
    body=models.CharField(max_length=150)

    def __str__(self):
        return self.title
        
    def summary(self):
        return self.body[:100]
