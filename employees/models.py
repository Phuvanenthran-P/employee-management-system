from django.db import models
from django.core.exceptions import ValidationError

class Employee(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.salary <= 0:
            raise ValidationError("Salary must be positive.")
