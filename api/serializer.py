from rest_framework import serializers
from .models import Student, Course, Enrollment

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        
class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = '__all__'
        
class ListCourseStudentsSerializer(serializers.ModelSerializer):
    course = serializers.ReadOnlyField(source = 'course.description')
    class Meta:
        model = Enrollment
        fields = ['course']
        
class ListStudentCoursesSerializer(serializers.ModelSerializer):
    student_name = serializers.ReadOnlyField(source = 'student.name')
    class Meta:
        model = Enrollment
        fields = ['student_name']