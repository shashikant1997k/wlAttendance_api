# Generated by Django 3.2.3 on 2021-05-24 06:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_auto_20210519_0944'),
        ('attendance', '0009_auto_20210521_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='empID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='employee.employee'),
        ),
    ]
