# Generated by Django 4.0.5 on 2022-08-01 11:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire_evaluation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionnaireevaluate',
            name='completed_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='questionnaireevaluate',
            name='published_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
