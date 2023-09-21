from django.contrib import admin

# Register your models here.
from .models import Tasks,Dc
admin.site.register(Tasks)
admin.site.register(Dc)