from django.contrib import admin
from projects.models import Project

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'start_date', 'end_date', 'get_workers', 'materials',)
    search_fields = ('project_name',)

    def get_workers(self, obj):
        return ", ".join(
            employee.name for employee in obj.workers.all()
        )

    get_workers.short_description = 'Workers'


admin.site.register(Project, ProjectAdmin)