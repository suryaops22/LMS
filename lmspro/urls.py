"""
URL configuration for lmspro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('lmsapp/', include('lmsapp.urls')),# 'lmsapp'))),#, namespace='lmsapp')),
   # Include your app's URLs here
    # path('lmsapp/courses/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/enrollments/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/contents/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/assignments/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/submissions/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/quizzes/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/quiz-questions/', include('lmsapp.urls')),  # Include your app's URLs here
    # path('lmsapp/quiz-answers/', include('lmsapp.urls')),  # Include your app's URLs here
]

