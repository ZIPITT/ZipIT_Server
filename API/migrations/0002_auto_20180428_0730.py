# Generated by Django 2.0.1 on 2018-04-28 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ideator',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
