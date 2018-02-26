from django.db import models

# Create your models here.
class Cadet(models.Model):    
	first = models.CharField(max_length=200)     
	last = models.CharField(max_length=200)     
	xnumber = models.CharField(max_length=8) 
 
	def __str__(self):       
		return self.last + ?, ? + self.first 
