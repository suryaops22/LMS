from django.shortcuts import render
from rest_framework import generics
from .models import UserDetail, Course, Enrollment, Content, Assignment, Submission, Quiz, QuizQuestion, QuizAnswer
from .serializers import (UserSerializer, CourseSerializer, EnrollmentSerializer, 
                          ContentSerializer, AssignmentSerializer, SubmissionSerializer, 
                          QuizSerializer, QuizQuestionSerializer, QuizAnswerSerializer)



# User Views
class UserListCreateView(generics.ListCreateAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserDetail.objects.all()
    serializer_class = UserSerializer
  

    def perform_update(self, serializer):
        serializer.save()

    def perform_destroy(self, instance):
        instance.delete()



# Course Views
class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field='id'
   

    def perform_update(self, serializer):
        print("Update method called")
        serializer.save()

    def perform_destroy(self, instance):
        print("Destroy method called")
        instance.delete()


    
    # permission_classes = [permissions.IsAuthenticated, IsCourseOwner]

    # def perform_destroy(self, instance):
    #     user = self.request.user
    #     if user.has_perm('delete_course', instance):
    #         instance.delete()
    #     else:
    #         raise PermissionDenied("You do not have permission to delete this course.")

# Enrollment Views
class EnrollmentListCreateView(generics.ListCreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

class EnrollmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    lookup_field='id'

# Content Views
class ContentListCreateView(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer

class ContentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerializer
    lookup_field='id'
     
    

# Assignment Views
class AssignmentListCreateView(generics.ListCreateAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer

class AssignmentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Assignment.objects.all()
    serializer_class = AssignmentSerializer
    lookup_field='id'

# Submission Views
class SubmissionListCreateView(generics.ListCreateAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer

class SubmissionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Submission.objects.all()
    serializer_class = SubmissionSerializer
    lookup_field='id'

# Quiz Views
class QuizListCreateView(generics.ListCreateAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer
    lookup_field='id'

# Quiz Question Views
class QuizQuestionListCreateView(generics.ListCreateAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer

class QuizQuestionRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizQuestion.objects.all()
    serializer_class = QuizQuestionSerializer
    lookup_field='id'

# Quiz Answer Views
class QuizAnswerListCreateView(generics.ListCreateAPIView):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer

class QuizAnswerRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = QuizAnswer.objects.all()
    serializer_class = QuizAnswerSerializer
    lookup_field='id'
