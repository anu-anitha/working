from django.db import models

# Create your models here.
class Exit(models.Model):
    value_choices=(
        (0,0),
        (1,1),
        (2,2),
        (3,3),
    )
    value=models.IntegerField(choices=value_choices)
    time=models.DateTimeField(auto_now_add = True)
