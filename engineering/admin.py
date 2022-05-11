from django.contrib import admin
from .models import Project, ProjectType
# Register your models here.
admin.site.register([Project, ProjectType])
