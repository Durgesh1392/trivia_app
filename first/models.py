from django.db import models
from datetime import datetime

# Create your models here.
class TestInfo(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)





    def __str__(self):
        return self.name
