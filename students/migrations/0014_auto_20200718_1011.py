# Generated by Django 2.2 on 2020-07-18 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20200718_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='school',
            name='school_manual',
            field=models.FileField(blank=True, null=True, upload_to='school_manual'),
        ),
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='student_photos'),
        ),
    ]
