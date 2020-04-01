# Generated by Django 2.2.5 on 2020-04-01 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refill', '0010_auto_20200324_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='phone_number',
            field=models.CharField(error_messages={'required': 'Please enter your Phone Number'}, help_text='Field to save the phone number of the user.', max_length=15, verbose_name='phone number'),
        ),
    ]