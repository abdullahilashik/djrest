from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('api/profiles/', include('profiles.urls')),
    path('admin/', admin.site.urls),
]
