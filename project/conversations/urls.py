from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.new_conversation, name='new_conversation'),
    path('<int:conversation_id>/', views.conversation_detail, name='conversation_detail'),
]