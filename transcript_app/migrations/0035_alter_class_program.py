# Generated by Django 4.0.4 on 2023-02-11 06:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0034_rename_course_class_program_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='class',
            name='program',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.program'),
        ),
    ]