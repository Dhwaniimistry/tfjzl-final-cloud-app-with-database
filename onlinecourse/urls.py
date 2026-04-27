from django.urls import path
from . import views

app_name = 'onlinecourse'

urlpatterns = [
    # Home / Course list
    path('', views.CourseListView.as_view(), name='index'),

    # Course detail
    path('course/<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),

    # Enroll
    path('course/<int:course_id>/enroll/', views.enroll, name='enroll'),

    # Auth
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('register/', views.registration_request, name='register'),

    # Submit exam
    path('<int:course_id>/submit/', views.submit, name='submit'),

    # Show result
    path(
        'course/<int:course_id>/submission/<int:submission_id>/result/',
        views.show_exam_result,
        name='show_exam_result'
    ),
]