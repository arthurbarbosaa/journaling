from django.contrib import admin
from django.urls import path
from journaling.views import journal_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', journal_list),
]
