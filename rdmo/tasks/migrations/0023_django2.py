# Generated by Django 2.2rc1 on 2019-03-26 13:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0022_remove_null_true'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ('uri',), 'verbose_name': 'Task', 'verbose_name_plural': 'Tasks'},
        ),
    ]
