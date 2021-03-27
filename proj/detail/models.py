from django.db import models

# Create your models here.\
class Services(models.Model):
    "Услуги"
    serv_name = models.CharField(max_length=200)

    def __str__(self):
        return self.serv_name

    class Meta:
        verbose_name = 'Госуслуга'
        verbose_name_plural = 'Госуслуги' 

class Ministries(models.Model):
    "Министерства"
    min_name = models.CharField(max_length=200)
    services = models.ManyToManyField(Services, verbose_name='Госуслуги')

    def __str__(self):
        return self.min_name

    class Meta:
        verbose_name = 'Ведомство'
        verbose_name_plural = 'Ведомства' 


class Problem(models.Model):
    "Проблема"
    prob_name = models.CharField("Проблема", max_length=200)
    ministries = models.ManyToManyField(Ministries, verbose_name="Ведомства")

    def __str__(self):
        return self.prob_name

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы' 
    
class Region(models.Model):
    "Регион"
    reg_name = models.CharField(max_length=200, verbose_name='Регион')
    problems = models.ManyToManyField(Problem , verbose_name='Проблемы')

    def __str__(self):
        return self.reg_name
    
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'    
   