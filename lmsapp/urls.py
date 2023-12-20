from django.urls import path
from .views import (
    UserListCreateView, UserRetrieveUpdateDestroyView, 
    CourseListCreateView, CourseRetrieveUpdateDestroyView, 
    EnrollmentListCreateView, EnrollmentRetrieveUpdateDestroyView,
    ContentListCreateView, ContentRetrieveUpdateDestroyView, 
    AssignmentListCreateView, AssignmentRetrieveUpdateDestroyView, 
    SubmissionListCreateView, SubmissionRetrieveUpdateDestroyView,
    QuizListCreateView, QuizRetrieveUpdateDestroyView,
    QuizQuestionListCreateView, QuizQuestionRetrieveUpdateDestroyView,
    QuizAnswerListCreateView, QuizAnswerRetrieveUpdateDestroyView
)
# print("Reached lmsapp/urls.py")
urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('courses/', CourseListCreateView.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroyView.as_view(), name='course-detail'),
    path('enrollments/', EnrollmentListCreateView.as_view(), name='enrollment-list'),
    path('enrollments/<int:pk>/', EnrollmentRetrieveUpdateDestroyView.as_view(), name='enrollment-detail'),
    path('contents/', ContentListCreateView.as_view(), name='content-list'),
    path('contents/<int:pk>/', ContentRetrieveUpdateDestroyView.as_view(), name='content-detail'),
    path('assignments/', AssignmentListCreateView.as_view(), name='assignment-list'),
    path('assignments/<int:pk>/', AssignmentRetrieveUpdateDestroyView.as_view(), name='assignment-detail'),
    path('submissions/', SubmissionListCreateView.as_view(), name='submission-list'),
    path('submissions/<int:pk>/', SubmissionRetrieveUpdateDestroyView.as_view(), name='submission-detail'),
    path('quizzes/', QuizListCreateView.as_view(), name='quiz-list'),
    path('quizzes/<int:pk>/', QuizRetrieveUpdateDestroyView.as_view(), name='quiz-detail'),
    path('quiz-questions/', QuizQuestionListCreateView.as_view(), name='quiz-question-list'),
    path('quiz-questions/<int:pk>/', QuizQuestionRetrieveUpdateDestroyView.as_view(), name='quiz-question-detail'),
    path('quiz-answers/', QuizAnswerListCreateView.as_view(), name='quiz-answer-list'),
    path('quiz-answers/<int:pk>/', QuizAnswerRetrieveUpdateDestroyView.as_view(), name='quiz-answer-detail')
]
