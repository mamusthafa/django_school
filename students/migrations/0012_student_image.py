# Generated by Django 2.2 on 2020-07-18 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0011_auto_20200718_0849'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='student_photos'),
        ),
    ]
