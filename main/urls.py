from . import views
from django.urls import path

urlpatterns = [
    path('timetable/', views.TimeTableAPIView.as_view()),
    path('test-list/', views.MainTestListAPIView.as_view()),
    path('test-create/', views.MainTestCreateAPIView.as_view()),
    path('group-list/', views.GroupListAPIView.as_view()),
    path('group-members/', views.GroupMembersListAPIView.as_view()),
    path('subject-list/', views.SubjectListAPIView.as_view()),
    path('take-subject/', views.TakeSubjectAPIView.as_view()),
    path('user-absence/', views.UserAbsenceListAPIView.as_view()),
    path('user-subject-list/', views.UserSubjectsListAPIView.as_view()),
    path('task-create/', views.TaskCreateAPIView.as_view()),

]
