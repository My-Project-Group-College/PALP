from django.contrib import admin
from .models import Course, Assessment, Question, Answer

admin.site.register(Course)
admin.site.register(Assessment)
admin.site.register(Question)
admin.site.register(Answer)