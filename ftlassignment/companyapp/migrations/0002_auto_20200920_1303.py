# Generated by Django 2.2.7 on 2020-09-20 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='tz',
            field=models.CharField(default='Europe/London', max_length=100),
        ),
    ]
