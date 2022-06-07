from django.contrib import admin
from django.urls import path, include
from api.views import CoursesStudent, StudentsViewSet, CoursesViewSet, EnrollmentViewSet, StudentCourses
from rest_framework import routers

router = routers.DefaultRouter()
router.register('students', StudentsViewSet, basename = 'Students')
router.register('courses', CoursesViewSet, basename = 'Courses')
router.register('enrollment', EnrollmentViewSet, basename = 'Enrollments')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('student/<int:pk>/enrollments', StudentCourses.as_view()),
    path('course/<int:pk>/enrollments', CoursesStudent.as_view())
]
