from django.urls import path, re_path

from .views import CourseListView, CourseDetailView, CourseInfoView, CommentsView

app_name = "course"

urlpatterns = [
    path('list/', CourseListView.as_view(), name='course_list'),
    re_path('course/(?P<course_id>\d+)/', CourseDetailView.as_view(), name='course_detail'),
    re_path('info/(?P<course_id>\d+)/', CourseInfoView.as_view(), name="course_info"),
    re_path('comment/(?P<course_id>\d+)/', CommentsView.as_view(), name="course_comments"),
]
