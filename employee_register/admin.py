from django.contrib import admin

# Register your models here.
from .models import Position, Employee, ActivityPeriod


admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(ActivityPeriod)