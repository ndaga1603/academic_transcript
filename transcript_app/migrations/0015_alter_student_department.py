# Generated by Django 4.0.4 on 2022-12-01 06:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0014_alter_class_course_alter_hod_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.department', verbose_name='belongs to (departiment)'),
        ),
    ]
