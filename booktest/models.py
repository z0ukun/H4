# coding=utf8
from django.db import models


# Create your models here.
class bookinfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub = models.DateTimeField()

    def __str__(self):
        return self.btitle.encode('utf-8')


class heroinfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    hbook = models.ForeignKey(bookinfo)

    def __str__(self):
        return self.hname.encode('utf-8')
