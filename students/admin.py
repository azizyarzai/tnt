from django.contrib import admin
from students.models import Student

# Register your models here.


class StudentModalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'age', 'updated']
    list_display_links = ['id',     'name']
    # list_per_page = 3
    search_fields = ['name', 'course']
    list_filter = ['updated', 'course', 'name']


admin.site.register(Student, StudentModalAdmin)
