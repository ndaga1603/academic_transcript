# Generated by Django 4.0.4 on 2022-12-04 09:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0025_overall_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='semester_student_result',
            old_name='semister',
            new_name='semester',
        ),
    ]