# Generated by Django 2.2.5 on 2021-10-14 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20211014_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('other', 'Other'), ('female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='user',
            name='language',
            field=models.CharField(blank=True, choices=[('kr', 'Korean'), ('en', 'English')], max_length=2),
        ),
    ]