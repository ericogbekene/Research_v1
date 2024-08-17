from django.contrib import admin
from .models import Department, Project, Writer, HireWriter, JobStatus

admin.site.register(Department)
admin.site.register(Project)
admin.site.register(Writer)
admin.site.register(HireWriter)
admin.site.register(JobStatus)
