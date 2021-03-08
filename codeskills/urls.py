"""
codeskills URL Configuration

"""
# Django
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

# Apps
from users import views as apis

#Password
from users.views import ChangePasswordView
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', apis.UserLogin.as_view(), name='login'),
    path('signup/', apis.UserSignup.as_view(), name='signup'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
