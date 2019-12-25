from django.urls import path, include, re_path
import xadmin
from django.views.generic import TemplateView
from django.views.static import serve

from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, IndexView, LogoutView
from sms.settings import MEDIA_ROOT, STATICFILES_DIRS


urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    # path('', TemplateView.as_view(template_name='index.html'),name='index'),
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name='register'),
    path('captcha/', include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/', ActiveUserView.as_view(), name='user_active'),
    path('forget/', ForgetPwdView.as_view(), name='forget_pwd'),

    path('org/', include('organization.urls', namespace='org')),
    path('course/', include('course.urls', namespace="courses")),
    path('uses/', include('users.urls', namespace='users')),
    # re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATIC_ROOT}),

    # re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT }),
    re_path(r'^static/(?P<path>.*)', serve, {"document_root": STATICFILES_DIRS}),

    path('ueditor/', include('DjangoUeditor.urls')),
]

handler404 = 'users.views.page_not_found'

handler500 = 'users.views.page_error'
