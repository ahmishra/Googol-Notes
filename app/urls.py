from django.urls import path
from . import views as v

app_name = 'app'

urlpatterns = [
    path('', v.HomePageListView.as_view(), name='all-notes'),
    path('note/new', v.NoteCreateView.as_view(), name='create-note'),
    path('note/detail/<int:pk>/', v.NoteDetailView.as_view(), name='detail-note'),
    path('note/update/<int:pk>/', v.NoteEditView.as_view(), name='update-note'),
    path('note/delete/<int:pk>/', v.NoteDeleteView.as_view(), name='delete-note'),
]
