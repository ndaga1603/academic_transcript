# Generated by Django 4.0.4 on 2022-11-29 23:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0006_overall_result_nta_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enrollment',
            name='student',
        ),
        migrations.AddField(
            model_name='enrollment',
            name='student',
            field=models.ManyToManyField(to='transcript_app.student'),
        ),
    ]