# Generated by Django 4.0.4 on 2022-12-01 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0011_alter_category_name_alter_class_class_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class_module',
            name='module_code',
        ),
        migrations.AddField(
            model_name='class_module',
            name='module_code',
            field=models.ManyToManyField(to='transcript_app.module', verbose_name='modules'),
        ),
    ]