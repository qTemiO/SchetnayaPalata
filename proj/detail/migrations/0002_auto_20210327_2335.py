# Generated by Django 3.1.7 on 2021-03-27 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detail', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ministries',
            name='min_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='problem',
            name='prob_name',
            field=models.CharField(max_length=200, verbose_name='Проблема'),
        ),
        migrations.AlterField(
            model_name='region',
            name='reg_name',
            field=models.CharField(max_length=200, verbose_name='Регион'),
        ),
        migrations.AlterField(
            model_name='services',
            name='serv_name',
            field=models.CharField(max_length=200),
        ),
    ]
