# Generated by Django 4.1.3 on 2022-12-13 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='lname',
            field=models.CharField(default='limbu', max_length=100),
        ),
        migrations.AddField(
            model_name='feature',
            name='name',
            field=models.CharField(default='sushil', max_length=100),
        ),
    ]