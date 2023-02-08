# Generated by Django 3.2.16 on 2023-02-03 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0052_meta'),
    ]

    operations = [
        migrations.AddField(
            model_name='value',
            name='user_comment',
            field=models.TextField(blank=True, help_text='The user comment stored for this value.', verbose_name='Comment'),
        ),
    ]