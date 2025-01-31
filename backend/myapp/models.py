from django.db import models

class Course(models.Model):
    course_code = models.CharField(max_length=10, unique=True)  # Example: "CS101"
    course_name = models.CharField(max_length=100)              # Example: "Introduction to Computer Science"
    credit = models.PositiveIntegerField()                     # Example: 3
    gpa_value = models.DecimalField(max_digits=3, decimal_places=2)  # Example: 3.75

    def __str__(self):
        return f"{self.course_code} - {self.course_name}"
