from django.db import models

class Problem(models.Model):
    "Класс проблемы как элемента диаграммы"
    name = models.CharField("Проблема", max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Проблема'
        verbose_name_plural = 'Проблемы' 

class Ministry(models.Model):
    "Модель ведомства с проблемами"
    name = models.CharField(verbose_name="Название ведомства", max_length=50)
    problems = models.ManyToManyField(Problem, related_name="problemas")

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Ведомство'
        verbose_name_plural = 'Ведомства'     

class ProblemCluster(models.Model):
    "Категория проблем"
    name = models.CharField(verbose_name="Категория проблем", max_length=100)
    ministries = models.ManyToManyField(Ministry, verbose_name="Ведомства", related_name='mynistries')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория проблем'
        verbose_name_plural = 'Категории проблем' 
    
class Diagram(models.Model):
    "Модель диаграммы"
    value = models.FloatField(verbose_name='Значение проблемы в диаграмме')
    problemcluster = models.ForeignKey(ProblemCluster, verbose_name="Категории проблем", on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Диаграмма'
        verbose_name_plural = 'Диаграммы' 

    def __str__(self):
        return self.problemcluster.name
    




"""
class Services(models.Model):
    "Услуги в которых возникает куча проблем"
    name = models.CharField(max_length=300)
    problems = models.ManyToManyField(Problem, verbose_name="Проблемы")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Госуслуга с проблемами'
        verbose_name_plural = 'Госуслуги с проблемами' 
"""
