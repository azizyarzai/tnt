from django.db import models
from django.forms import ValidationError

# Create your models here.

COURSES = [
    ("001", "Python"),
    ("002", "JavaScript"),
]


def min_age(val):
    if val < 18:
        raise ValidationError("Age should be greater than 18.")


class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField(validators=[min_age])
    height = models.DecimalField(default=150.3, decimal_places=2, max_digits=5)
    course = models.CharField(max_length=120, choices=COURSES, default="002")
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name + " - " + str(self.id)
        # return f"{name} - {id}"
        # return ""
