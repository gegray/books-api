from django.db import models

# Create your models here.
class Books(models.Model):    
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	pubdate = models.CharField(max_length=200)
	publisher = models.CharField(max_length=200)
	summary = models.CharField(max_length=2000)
	price = models.FloatField()
	url = models.URLField(max_length=2000)
	coverimg = models.URLField(max_length=2000)