from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Student, Course, Enrollment
from .serializer import StudentSerializer, CourseSerializer, EnrollmentSerializer, ListCourseStudentsSerializer, ListStudentCoursesSerializer

class StudentsViewSet(viewsets.ModelViewSet):
    """Show all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
class CoursesViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class EnrollmentViewSet(viewsets.ModelViewSet):
    """Show all enrollments"""
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class StudentCourses(generics.ListAPIView):
    """List all student courses """
    
    def get_queryset(self):
        return Enrollment.objects.filter(student_id = self.kwargs['pk'])
    serializer_class = ListCourseStudentsSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CoursesStudent(generics.ListAPIView):
    """List all students in course"""
    
    def get_queryset(self):
        return Enrollment.objects.filter(course_id = self.kwargs['pk'])
    serializer_class = ListStudentCoursesSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]