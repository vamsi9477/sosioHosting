# Generated by Django 2.1.1 on 2018-11-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sc1', '0003_sosio_res'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sosio',
            name='names',
            field=models.CharField(max_length=100),
        ),
    ]
