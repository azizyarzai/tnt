from django.contrib import admin
from students.models import Student, Course

# Register your models here.


class StudentModalAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'course', 'age', 'updated']
    list_display_links = ['id',     'name']
    # list_per_page = 3
    search_fields = ['name', 'course__title']
    list_filter = ['updated', 'course', 'name']


class CoursreModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'from_date', 'to_date']


admin.site.register(Student, StudentModalAdmin)
admin.site.register(Course, CoursreModelAdmin)
