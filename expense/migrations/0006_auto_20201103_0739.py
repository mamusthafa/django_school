# Generated by Django 3.1 on 2020-11-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expense', '0005_auto_20201103_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='expense_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]