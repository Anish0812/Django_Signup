from django.db import models

class StudentModel(models.Model):
    name=models.CharField(primary_key=True,max_length=100)
    feedback=models.CharField(max_length=20)

    def __str__(self):
        return self.name
