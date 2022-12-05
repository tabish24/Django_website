from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('Signup/', include('Signup.urls')),
    path('Signupdata/', include('Signup.urls')),
    path('login/', include('Login.urls')),
    path('admin/', admin.site.urls),
]