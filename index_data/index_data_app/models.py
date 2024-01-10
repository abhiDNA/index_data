from django.db import models

class Nifty50(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()

    # def __str__(self):
    #     return self.entry_date

class NiftyMidcap50(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()

class NiftyMidcap150(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()

class NiftyNext50(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()

class NiftySmallcap50(models.Model):
    date = models.DateField()
    open = models.FloatField()
    high = models.FloatField()
    low = models.FloatField()
    close = models.FloatField()
    shares_traded = models.IntegerField()
    turnover = models.FloatField()

