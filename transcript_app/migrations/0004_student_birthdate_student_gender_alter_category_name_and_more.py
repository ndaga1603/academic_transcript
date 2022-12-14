# Generated by Django 4.0.4 on 2022-11-29 22:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0003_remove_module_form_four_index_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='birthdate',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default=1, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(choices=[('OD', 'ORDINARY DIPLOMA'), ('BCH', 'BACHELOR DEGREE'), ('MS', 'MASTERS')], max_length=20),
        ),
        migrations.AlterField(
            model_name='nta_level',
            name='level',
            field=models.CharField(choices=[('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8')], max_length=20),
        ),
        migrations.AlterField(
            model_name='nta_level',
            name='number_of_semesters',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(6), django.core.validators.MinValueValidator(2)]),
        ),
    ]
