from django.contrib import admin

# Register your models here.


from .models import sampleData

class sampleDataAdmin(admin.ModelAdmin):
    pass
admin.site.register(sampleData, sampleDataAdmin)
