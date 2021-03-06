# Generated by Django 4.0.3 on 2022-03-27 01:56

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0010_remove_result_one_record_per_day_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='created_at',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='result',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
