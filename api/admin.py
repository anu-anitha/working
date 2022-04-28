from django.contrib import admin

# Register your models here.
from .models import TableApi,SkyvyApi
# Register your models here.
admin.site.register(TableApi)
admin.site.register(SkyvyApi)