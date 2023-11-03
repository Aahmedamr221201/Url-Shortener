from django.db import models

# Create your models here.
class Url(models.Model):
	original_url = models.CharField(max_length = 1000 , null = False, blank=False)
	unique_id = models.CharField(max_length=200 , blank = False , null = False , unique = True)