from django.contrib import admin
from .models import Student

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['user', 'grade', 'university', 'course']
    search_fields = [
        'user__first_name',
        'user__last_name',
        'course', 'university']