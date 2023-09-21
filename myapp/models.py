from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    my_list = models.JSONField(default=list)


