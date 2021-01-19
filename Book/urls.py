from django import urls
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('BookShelves.urls')),
    path('', include('registration.urls')),
    path('', include('django.contrib.auth.urls'))
]
