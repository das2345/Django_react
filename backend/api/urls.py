from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.CreateNoteListView.as_view(), name='note-list'),
    path('notes/delete/<int:pk>/',views.noteDelete.as_view(),name='delete-note')

]