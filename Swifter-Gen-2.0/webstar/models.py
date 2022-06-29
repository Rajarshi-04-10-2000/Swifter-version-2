from django.db import models

# Create your models here.


class Tranporter(models.Model):
    dname = models.CharField(max_length=50, default='0000000')
    license_no = models.CharField(
        max_length=50, default='0000000')
    dphone = models.CharField(max_length=50, default='0000000')
    v_no = models.CharField(max_length=50, default='0000000')
    v_type = models.CharField(max_length=50, default='0000000')
    permit_wt = models.CharField(
        max_length=50, default='0000000')
    v_status = models.CharField(max_length=50, default='Available')

    def __str__(self):
        return self.dname


class Company(models.Model):
    user_name = models.CharField(max_length=50, default='0000000')
    g_type = models.CharField(max_length=50, default='0000000')
    src = models.CharField(max_length=50, default='0000000')
    dest = models.CharField(max_length=50, default='0000000')
    weight = models.CharField(max_length=50, default='0000000')
    dist = models.CharField(max_length=50, default='0000000')

    def __str__(self):
        return self.user_name
