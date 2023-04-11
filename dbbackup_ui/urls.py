from django.urls import re_path
from .views import BackupView

urlpatterns = [
    re_path(r'^backup-database-and-media/$', BackupView.as_view(), name="backup_view"),
]
