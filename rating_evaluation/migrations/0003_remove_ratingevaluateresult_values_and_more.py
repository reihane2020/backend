# Generated by Django 4.0.5 on 2022-07-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rating_evaluation', '0002_ratingevaluatevalue_ratingevaluateresult'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ratingevaluateresult',
            name='values',
        ),
        migrations.AddField(
            model_name='ratingevaluateresult',
            name='rating',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.DeleteModel(
            name='RatingEvaluateValue',
        ),
    ]
