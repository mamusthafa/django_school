# Generated by Django 2.2 on 2020-09-19 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=250),
        ),
    ]
