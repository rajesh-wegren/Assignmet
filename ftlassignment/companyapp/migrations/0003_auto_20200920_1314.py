# Generated by Django 2.2.7 on 2020-09-20 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companyapp', '0002_auto_20200920_1303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='member',
        ),
        migrations.AddField(
            model_name='member',
            name='member',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='companyapp.Period'),
            preserve_default=False,
        ),
    ]
