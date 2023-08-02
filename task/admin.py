from django.contrib import admin
from .models import Task
# Register your models here.

# Para que se vea la fecha de creacion
class TaskAdmin(admin.ModelAdmin):
    readonly_fields=("created",)


admin.site.register(Task, TaskAdmin)
