from django.db import models

# Create your models here.

class Consultant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=300)

    def __str__(self):
        return f'Consultant_{self.id}_{self.name}'

class Entrepreneur(models.Model):
    id = models.AutoField(primary_key=True)
    consultant_id = models.ForeignKey(Consultant, on_delete=models.CASCADE, related_name='entrepreneur')
    name = models.CharField(max_length=250)
    email = models.CharField(max_length=300)
    def __str__(self):
        return f'Entrepreneur_{self.id}_{self.name}'

class Course(models.Model):
    id = models.AutoField(primary_key=True)
    consultant_id = models.ForeignKey(Consultant, on_delete=models.PROTECT, related_name='consultant_course')
    course_title = models.CharField(max_length=250)
    course_description = models.TextField(blank=True)

    def __str__(self):
        return f'Course_{self.id}_{self.course_title}'

class Course_module(models.Model):
    id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_module')
    module_title = models.CharField(max_length=250)
    module_description = models.TextField(blank=True)

    def __str__(self):
        return f'Module_{self.id}_{self.module_title}'

# store course_content with dynamic file name
def store_course_content(instance, filename):
    return f'module_content_image_id{instance.course_content.id}_{filename}'

class Course_content(models.Model):
    id = models.AutoField(primary_key=True)
    module_id = models.ForeignKey(Course_module, on_delete=models.CASCADE, related_name='course_content')
    content_title = models.TextField(blank=True)
    content_image = models.ImageField(upload_to=store_course_content, default=None)
    content_video = models.FileField(upload_to=store_course_content, default=None)

    def __str__(self):
        return f'Content_{self.id}_{self.content_title}'

class Course_quiz(models.Model):
    id = models.AutoField(primary_key=True)
    module_id = models.ForeignKey(Course_module, on_delete=models.CASCADE, related_name='course_quiz')
    quiz_title = models.CharField(max_length=250)
    quiz_description = models.TextField(blank=True)

    def __str__(self):
        return f'Quiz_{self.id}_{self.quiz_title}'

class Quiz_question(models.Model):
    id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey(Course_quiz, on_delete=models.CASCADE,related_name='quiz_question')
    question_title = models.TextField()
    question = models.TextField()
    question_binary = models.BinaryField(max_length=None, blank=True)
    difficulty = models.IntegerField()

    def __str__(self):
        return f'Question_{self.id}_{self.question_title}'


class Answer(models.Model):
    id = models.AutoField(primary_key=True)
    entr_id = models.ForeignKey(Entrepreneur, on_delete=models.CASCADE, related_name='entr_answer')
    quiz_question = models.ForeignKey(Quiz_question, on_delete=models.CASCADE, related_name='quiz_name')
    answer = models.BinaryField(max_length=None, blank=True)
    answer_par = models.TextField()

    def __str__(self):
        return f'Answer_{self.id}_{self.entr_id}'