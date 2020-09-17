"""trivia_app URL Configuration
Description:
name : name of the person who take quize
time : To capture quiz time
q1_a:question one response
q2_a:question tw0 response




"""

from django.db import models
from datetime import datetime

# Create your models here.
class TestInfo(models.Model):
    name = models.CharField(max_length=200)
    time = models.DateTimeField(default=datetime.now)





    def __str__(self):
        return self.name
