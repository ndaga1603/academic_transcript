# Generated by Django 4.0.4 on 2022-12-01 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0016_delete_semester_student_result'),
    ]

    operations = [
        migrations.CreateModel(
            name='Semester_Student_result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academic_year', models.CharField(max_length=10)),
                ('CA', models.FloatField()),
                ('FE', models.FloatField()),
                ('status', models.CharField(choices=[('pass', 'pass'), ('fail', 'fail')], max_length=5)),
                ('module_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.module')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.student', verbose_name='student name')),
            ],
        ),
    ]