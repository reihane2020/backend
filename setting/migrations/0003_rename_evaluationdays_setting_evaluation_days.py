# Generated by Django 4.0.5 on 2022-08-02 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setting', '0002_setting_evaluationdays'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setting',
            old_name='evaluationDays',
            new_name='evaluation_days',
        ),
    ]
