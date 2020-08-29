# Generated by Django 3.1 on 2020-08-29 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='bursary',
            field=models.CharField(choices=[('nsfas', 'NSFAS')], max_length=10),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=140),
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 1), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12)], default=1, max_length=2),
        ),
        migrations.AlterField(
            model_name='student',
            name='university',
            field=models.CharField(max_length=50),
        ),
    ]
