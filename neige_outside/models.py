from django.db import models

class Post(models.Model):
	text_fr = models.CharField(max_length=7000)
	text_en = models.CharField(max_length=7000)
	pub_date = models.DateTimeField('date published')
