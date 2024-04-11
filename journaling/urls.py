from django.urls import path
from . import views
from journaling.views import journal_list, save_journal

urlpatterns = [
    path('', journal_list, name="journal_list"),
    path('save_journal/', save_journal, name='save_journal'),
]