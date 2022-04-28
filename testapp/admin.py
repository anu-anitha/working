from django.contrib import admin
from .models import Exit
# Register your models here.

class ExitAdmin(admin.ModelAdmin):
    list_display=['value','time']

admin.site.register(Exit,ExitAdmin)
