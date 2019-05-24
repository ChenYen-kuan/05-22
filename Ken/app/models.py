from django.db import models

# Create your models here.
class Information(models.Model):
	name = models.CharField(max_length=20)
	department = models.CharField(max_length=20)
	student_ID = models.CharField(max_length=20)
	interest = models.CharField(max_length=50, blank=True)

	def __str__(self):
		return self.name 
