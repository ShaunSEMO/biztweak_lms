from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Consultant)
admin.site.register(models.Entrepreneur)
admin.site.register(models.Course)
admin.site.register(models.Course_module)
admin.site.register(models.Course_content)
admin.site.register(models.Course_quiz)
admin.site.register(models.Quiz_question)
admin.site.register(models.Answer)