from django.contrib import admin

from main.models import Student


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'first_name', 'last_name', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('first_name', 'last_name',)
