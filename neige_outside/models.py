from django.db import models


class Post(models.Model):
    title_fr = models.CharField(max_length=200)
    text_fr = models.CharField(max_length=7000)
    url_fr = models.CharField(max_length=200)

    title_en = models.CharField(max_length=200)
    text_en = models.CharField(max_length=7000)
    url_en = models.CharField(max_length=200)

    pub_date = models.DateTimeField('date published')

    def __str__(self):              # __unicode__ on Python 2
        return self.title_en
