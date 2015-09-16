from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=10000)
    preview = models.CharField(max_length=104)

    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.title
