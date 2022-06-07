from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    birth_date = models.DateField(auto_now=False, auto_now_add=False)
    
    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'
    
    def __str__(self) -> str:
        return self.name
    
    def to_json(self):
        return {
            'id': self.pk,
            'name': self.name,
            'age': self.age,
            'birth_date': self.birth_date
        }

class Course(models.Model):
    LEVEL = (
        ('B', 'Basic'),
        ('I', 'Intermediary'),
        ('A', 'Advanced')
    )
    code = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, null=False, default='B')
    
    class Meta:
        verbose_name = 'course'
        verbose_name_plural = 'courses'
    
    def __str__(self) -> str:
        return self.description
    
    def to_json(self):
        return {
            'id': self.pk,
            'code': self.code,
            'description': self.description,
            'level': self.level
        }

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete = models.CASCADE)
    course = models.ForeignKey(Course, on_delete = models.CASCADE)
    
    class Meta:
        verbose_name = 'enrollment'
        verbose_name_plural = 'enrollments'