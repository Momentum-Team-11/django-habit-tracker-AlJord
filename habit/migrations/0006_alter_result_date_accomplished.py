# Generated by Django 4.0.3 on 2022-03-27 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('habit', '0005_alter_habit_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='date_accomplished',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]