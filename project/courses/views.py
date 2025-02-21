from django.shortcuts import render, redirect, get_object_or_404
from .models import Course, Assessment
from .forms import CourseForm

def create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.creator = request.user
            course.save()
            return redirect('course_detail', course.id)
    else:
        form = CourseForm()
    return render(request, 'create_course.html', {'form': form})

def course_detail(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    return render(request, 'course_detail.html', {'course': course})


def assessment_view(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    assessments = Assessment.objects.filter(course=course)
    return render(request, 'assessment.html', {
        'course': course,
        'assessments': assessments
    })

def take_test(request, assessment_id):
    assessment = get_object_or_404(Assessment, id=assessment_id)
    questions = Question.objects.filter(assessment=assessment).order_by('order')
    return render(request, 'take_test.html', {
        'assessment': assessment,
        'questions': questions
    })