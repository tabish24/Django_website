from django.contrib import admin
from django.urls import path, include
from Kspl import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Kspl/', include('Kspl.urls')) 
]
