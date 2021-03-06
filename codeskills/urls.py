"""
codeskills URL Configuration

"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from users import views as user_views
from home import views as home_views
from users import api_views as apis


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', user_views.login_view, name='login'),
    path('logout/', user_views.logout_view, name='logout'),
    path('signup/', user_views.signup, name='signup'),
    path('home/', home_views.home, name='home'),
    path('editor/', home_views.editor, name='editor'),
    path('api/v1/login-api', apis.UserLogin.as_view(), name='login-api'),
    path('api/v1/signup-api', apis.UserSignup.as_view(), name='signup-api'),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
