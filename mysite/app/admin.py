from django.contrib import admin
from .models import Information

# Register your models here.

class InformationAdmin(admin.ModelAdmin):
	list_display = ('name', 'department', 'student_ID','interest')

admin.site.register(Information)
