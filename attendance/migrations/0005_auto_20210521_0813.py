# Generated by Django 3.2.3 on 2021-05-21 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_alter_attendance_daydate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timing_in',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='timing_out',
            field=models.TimeField(),
        ),
    ]
