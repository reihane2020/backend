# Generated by Django 4.0.5 on 2022-07-26 13:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rating_evaluation', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingEvaluateValue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RatingEvaluateResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('evaluate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rating_evaluation.ratingevaluate')),
                ('evaluated_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('values', models.ManyToManyField(blank=True, to='rating_evaluation.ratingevaluatevalue')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]