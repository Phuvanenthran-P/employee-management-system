from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "role", "salary", "created_at")
    list_filter = ("role",)
    search_fields = ("name", "role")
    ordering = ("-created_at",)
