# Generated by Django 3.2.16 on 2023-02-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0068_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='help_accordion1',
            field=models.TextField(blank=True, help_text='The help text for this question to be displayed in the first accordion.', null=True, verbose_name='Help (accordion, 1)'),
        ),
        migrations.AddField(
            model_name='question',
            name='help_accordion2',
            field=models.TextField(blank=True, help_text='The help text for this question to be displayed in the second accordion.', null=True, verbose_name='Help (accordion, 2)'),
        ),
    ]