from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Custom User Model (Extending AbstractUser for custom user model)
class UserDetail(User):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('instructor', 'Instructor'),
        ('admin', 'Admin'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

# groups = models.ManyToManyField('auth.Group', related_name='userdetail_groups')

# Course Model
class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    instructor = models.ForeignKey(UserDetail, on_delete=models.SET_NULL, null=True, related_name='courses_taught')

    def __str__(self):
        return self.title

# Enrollment Model
class Enrollment(models.Model):
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='enrollments')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='enrollments')
    enrollment_date = models.DateField()

# Content Model
class Content(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='contents')
    title = models.CharField(max_length=255)
    body = models.TextField()

# Assignment Model
class Assignment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assignments')
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()

# Submission Model
class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='submissions')
    submission_date = models.DateField()
    content = models.TextField()

# Quiz Model
class Quiz(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='quizzes')
    title = models.CharField(max_length=255)

# Quiz Question Model
class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    question_text = models.TextField()

# Quiz Answer Model
class QuizAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(UserDetail, on_delete=models.CASCADE, related_name='quiz_answers')
    answer = models.TextField()


# AbstractUser.groups.field.related_name = 'auth_user_groups'