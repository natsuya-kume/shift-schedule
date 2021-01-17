from django.contrib import admin
from .models import Schedule
from .models import Shift

# Register your models here.
admin.site.register(Schedule)
admin.site.register(Shift)