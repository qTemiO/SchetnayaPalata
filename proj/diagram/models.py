from django.db import models

class Diagram(models.Model):
    "Модель диаграммы проблемы"
    value = models.FloatField(verbose_name='Значение проблемы в диаграмме')
    problem = models.CharField(verbose_name='Проблема', max_length=128)

    def __str__(self):
        return self.problem

    class Meta:
        verbose_name = 'Диаграмма'
        verbose_name_plural = 'Диаграммы' 
    
class Region(models.Model):
    "Модель региона с диаграмами проблемы для него"
    name = models.CharField(verbose_name="Навание региона", max_length=50)
    diagram = models.ManyToManyField(Diagram, related_name="diagrams")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы' 

class Problem(models.Model):
    "Класс проблемы как элемента классификации"
    name = models.CharField("Проблема", max_length=300)

    def __str__(self):
        return self.name
    

class Service(models.Model):
    "Услуги"
    name = models.CharField(verbose_name="Услуга", max_length=100)
    problem =  models.ManyToManyField(Problem, verbose_name="Проблемы", related_name=problems)

    def __str__(self):
        return self.name
    