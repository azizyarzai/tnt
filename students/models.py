from django.db import models
from django.forms import ValidationError
from django.db.models.signals import pre_save, post_save
import datetime
import datetime

datetime.datetime.today()

# Create your models here.

COURSES = [
    ("001", "Python"),
    ("002", "JavaScript"),
]


def min_age(val):
    if val < 18:
        raise ValidationError("Age should be greater than 18.")


class StudentModalManager(models.Manager):
    # def all(self):
    #     return self.filter(height__gt=160)

    def get_javascript_students(self):
        return self.filter(course='002')


class Student(models.Model):
    name = models.CharField(max_length=150, error_messages={
        "blank": 'Please fill the field',
        'unique': 'Duplicate value'
    }, unique=True, help_text="Please be carful this field must be unique.")
    date_of_birth = models.DateField(null=True, blank=True)
    height = models.DecimalField(default=150.3, decimal_places=2, max_digits=5)
    course = models.CharField(max_length=120, choices=COURSES, default="002")
    image = models.ImageField(upload_to="students", null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = StudentModalManager()

    @property
    def age(self):
        if self.date_of_birth:
            year = self.date_of_birth.year
            current = datetime.date.today()
            return current.year - year

    def __str__(self):
        return self.name + " - " + str(self.id)
        # return f"{name} - {id}"
        # return ""

    def save(self, *args, **kwargs):
        # print("save called")
        # self.age = self.age + self.age * 0.1
        return super().save(*args, **kwargs)


# def student_post_save_handler(sender, instance, created, *args, **kwargs):
#     print("post save called")
#     if created:
#         instance.age = instance.age + instance.age * 0.1
#         instance.save()


# # pre_save.connect(student_post_save_handler, sender=Student)
# post_save.connect(student_post_save_handler, sender=Student)
