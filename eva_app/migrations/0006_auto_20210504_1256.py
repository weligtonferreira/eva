# Generated by Django 3.2 on 2021-05-04 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva_app', '0005_alter_event_autor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='dataHora',
        ),
        migrations.AddField(
            model_name='event',
            name='data',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='hora',
            field=models.TimeField(auto_now=True, null=True),
        ),
    ]
