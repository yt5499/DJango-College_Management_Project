# Generated by Django 4.0.3 on 2022-05-06 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0011_auto_20200508_0913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentextra',
            name='cl',
            field=models.CharField(choices=[('Select one', 'Select one'), ('First Year', 'First Year'), ('DSE', 'DSE')], default='Select one', max_length=10),
        ),
    ]
