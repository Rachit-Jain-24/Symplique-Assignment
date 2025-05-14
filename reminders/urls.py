from django.urls import path
from . import views

urlpatterns = [
    path('reminders/', views.reminder_list_create, name='reminder-list-create'),
]
