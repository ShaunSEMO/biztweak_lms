from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models


# Create your views here.
@login_required
def home(request):
    logged_user = request.user
    user_last_login = logged_user.last_login
    courses = models.Course.objects.all()
    return render(request, 'lms_main/home.html', {'logged_user':logged_user, 'courses': courses, 'user_last_login':user_last_login})

@login_required
def view_course(request, id):
    logged_user = request.user
    user_last_login = logged_user.last_login
    course = models.Course.objects.get(id=id)
    course_modules = models.Course_module.objects.filter(course_id=course.id)
    return render(request, 'lms_main/view_course.html', {'logged_user':logged_user, 'course':course, 'user_last_login':user_last_login, 'course_modules': course_modules})

@login_required
def enroll_course(request, id):
    course = models.Course.objects.get(id=id)
    course_modules = models.Course_module.objects.filter(course_id=course.id)
    # course_content = models.Course_content.objects.filter(module_id=)
    return render(request, 'lms_main/enroll_course.html', {'course':course, 'course_modules':course_modules})

@login_required
def start_module(request, id):
    course_content = models.Course_content.objects.filter(module_id=id)
    current_module = models.Course_module.objects.get(id=id) 
    course_modules = models.Course_module.objects.filter(course_id=current_module.course_id)
    course = models.Course.objects.get(id=current_module.course_id)


    return render(request, 'lms_main/start_module.html', {'course_content':course_content, 'current_module': current_module, 'course_modules': course_modules})