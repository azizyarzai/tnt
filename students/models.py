from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    course = models.CharField(max_length=120)
    is_passed = models.BooleanField(default=True)
    last_name = models.CharField(max_length=80)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    height = models.DecimalField(default=150.3, decimal_places=2, max_digits=5)

    def __str__(self):
        return self.name + " - " + str(self.id)
        # return f"{name} - {id}"
        # return ""
