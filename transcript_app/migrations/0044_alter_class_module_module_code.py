# Generated by Django 4.0.4 on 2023-02-19 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0043_student_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class_module',
            name='module_code',
            field=models.ManyToManyField(related_name='modules', to='transcript_app.module', verbose_name='modules'),
        ),
    ]
