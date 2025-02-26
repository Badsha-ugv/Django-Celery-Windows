from django.db import models

# Create your models here.

class Counter(models.Model):
    count = models.IntegerField(default=0)

    def __str__(self):
        return str(self.count)
    