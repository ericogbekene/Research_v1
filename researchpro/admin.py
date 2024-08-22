from django.contrib import admin
from .models import Department, Project, Writer, HireWriter, JobStatus

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'department', 'number_of_pages', 'doctype', 'project_level', 'project_type', 'author', 'created_at')
    list_filter = ('department', 'project_level', 'project_type', 'doctype')
    search_fields = ('title', 'keywords', 'author__username')

class JobStatusInline(admin.TabularInline):
    model = JobStatus
    extra = 0 

@admin.register(Writer)
class WriterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'department', 'status', 'experience', 'rating', 'total_jobs',)
    list_filter = ('department', 'status', 'experience')
    search_fields = ('name__username', 'email')
    inlines = [JobStatusInline]

    def total_jobs(self, obj):
        return JobStatus.objects.filter(researcher=obj).count()
    total_jobs.short_description = 'Total Jobs'
@admin.register(HireWriter)
class HireWriterAdmin(admin.ModelAdmin):
    list_display = ('project_topic', 'get_writer_name', 'email', 'phone', 'job_status')
    search_fields = ('project_topic', 'get_writer_name', 'email')

    def get_writer_name(self, obj):
        return obj.writer.name.username if obj.writer.name else None
    get_writer_name.short_description = 'Writer Name'

@admin.register(JobStatus)
class JobStatusAdmin(admin.ModelAdmin):
    list_display = ('project', 'researcher', 'status')
    list_filter = ('status',)
    search_fields = ('project__title', 'researcher__name')
