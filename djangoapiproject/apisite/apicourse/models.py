from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    time_start = models.DateField()
    time_finish = models.DateField()

    def __str__(self):
        return self.name
