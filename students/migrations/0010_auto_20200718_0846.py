# Generated by Django 2.2 on 2020-07-18 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0009_auto_20200718_0828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to='profile_pics'),
        ),
    ]
