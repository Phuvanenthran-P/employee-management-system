from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.db.models import Q
from .models import Employee
from .forms import EmployeeForm

class EmployeeListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    permission_required = "employees.view_employee"
    model = Employee
    template_name = "employees/employee_list.html"
    context_object_name = "employees"
    ordering = ["-created_at"]
    paginate_by = 5

    def get_queryset(self):
        queryset = Employee.objects.all().order_by("-created_at")

        query = self.request.GET.get("q")
        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) |
                Q(role__icontains=query)
            )

        return queryset


class EmployeeCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "employees.add_employee"
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")


class EmployeeUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    permission_required = "employees.change_employee"
    model = Employee
    form_class = EmployeeForm
    template_name = "employees/employee_form.html"
    success_url = reverse_lazy("employee_list")


class EmployeeDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    permission_required = "employees.delete_employee"
    model = Employee
    template_name = "employees/employee_confirm_delete.html"
    success_url = reverse_lazy("employee_list")
