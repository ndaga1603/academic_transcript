# Generated by Django 4.0.4 on 2022-11-29 22:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0004_student_birthdate_student_gender_alter_category_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='birthdate',
            field=models.DateField(),
        ),
    ]
