# Generated by Django 4.0.4 on 2023-02-11 05:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0030_remove_student_department'),
    ]

    operations = [
        migrations.AlterField(
            model_name='overallresult',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.student'),
        ),
    ]