from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_course, name='create_course'),
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
    path('course/<int:course_id>/assessment/', views.assessment_view, name='assessment'),
    path('assessment/<int:assessment_id>/', views.take_test, name='take_test'),
]