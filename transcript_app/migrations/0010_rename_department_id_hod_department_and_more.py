# Generated by Django 4.0.4 on 2022-11-30 07:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transcript_app', '0009_alter_category_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hod',
            old_name='department_id',
            new_name='department',
        ),
        migrations.AlterField(
            model_name='class',
            name='NTA_level',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.nta_level', verbose_name='NTA_level'),
        ),
        migrations.AlterField(
            model_name='class_module',
            name='class_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.class', verbose_name='class'),
        ),
        migrations.AlterField(
            model_name='course',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transcript_app.department', verbose_name='departiment'),
        ),
    ]