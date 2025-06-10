from django.urls import path
from . import views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static

app_name='users'

urlpatterns = [
    path('register/',views.Register.as_view(),name='register'),
    path('login/',authentication_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',authentication_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',views.profile,name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)