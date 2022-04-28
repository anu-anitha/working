from django.db import models

# Create your models here.
class TableApi(models.Model):
    table_no = models.IntegerField()
    time=models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('table_no',)
        verbose_name = 'Table'
        verbose_name = 'Tables'

    def __str__(self):
        return str(self.table_no)


class SkyvyApi(models.Model):
    tab_no=models.CharField(max_length=20)
    start_time=models.DateTimeField(auto_now_add=True)
    end_time=models.DateTimeField(auto_now=True)
