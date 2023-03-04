from django.db import models
from django.utils import timezone


    
class Document(models.Model):
	title = models.CharField(max_length=100)
	docs_file = models.FileField(blank=True,upload_to='Files')
	description = models.TextField()
	date_posted = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.title


        
