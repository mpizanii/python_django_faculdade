from django.urls import path
from .views import event_list, event_create, event_delete

urlpatterns = [
    path('', event_list, name='event_list'),
    path('create/', event_create, name='event_create'),
    path('delete/<int:pk>/', event_delete, name='event_delete'),
]