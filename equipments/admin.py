from django.contrib import admin
from .models import Equipment, Repairing
# Register your models here.

admin.site.register([Equipment, Repairing])