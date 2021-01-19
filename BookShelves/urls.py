from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('Remove/<item_id>', views.remove, name='removeBook'),
    path('Update/<item_id>', views.update, name='updateBook'),
    path('Profile', views.profile, name='profile'),
]
