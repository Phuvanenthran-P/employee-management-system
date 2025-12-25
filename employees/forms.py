from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

    def clean_salary(self):
        salary = self.cleaned_data.get("salary")

        if salary <= 0:
            raise forms.ValidationError("Salary must be greater than zero.")

        if salary < 5000:
            raise forms.ValidationError("Salary is unrealistically low.")

        return salary

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get("role")
        salary = cleaned_data.get("salary")

        if role and salary:
            if role.lower() == "intern" and salary > 15000:
                raise forms.ValidationError(
                    "Intern salary cannot exceed 15,000."
                )

        return cleaned_data
