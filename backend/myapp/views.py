from django.shortcuts import render, redirect
from .forms import CourseForm
from .models import Course
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_gpa')  # Redirect to the total GPA page
    else:
        form = CourseForm()
    return render(request, 'add_course.html', {'form': form})

def view_gpa(request):
    courses = Course.objects.all()
    total_credits = sum(course.credit for course in courses)
    total_weighted_gpa = sum(course.credit * course.gpa_value for course in courses)
    total_gpa = total_weighted_gpa / total_credits if total_credits > 0 else 0

    return render(request, 'view_gpa.html', {
        'courses': courses,
        'total_gpa': round(total_gpa, 2)
    })

# Add these new API views
@csrf_exempt  # Only for development! Remove in production
def api_courses(request):
    if request.method == 'GET':
        courses = Course.objects.all()
        courses_data = [{
            'id': course.id,
            'course_code': course.course_code,
            'course_name': course.course_name,
            'credit': course.credit,
            'gpa_value': float(course.gpa_value)
        } for course in courses]
        return JsonResponse(courses_data, safe=False)
    
    elif request.method == 'POST':
        data = json.loads(request.body)
        try:
            course = Course.objects.create(
                course_code=data['course_code'],
                course_name=data['course_name'],
                credit=data['credit'],
                gpa_value=data['gpa_value']
            )
            return JsonResponse({
                'id': course.id,
                'course_code': course.course_code,
                'course_name': course.course_name,
                'credit': course.credit,
                'gpa_value': float(course.gpa_value)
            })
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

