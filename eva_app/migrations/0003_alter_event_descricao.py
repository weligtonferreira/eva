# Generated by Django 3.2 on 2021-05-03 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva_app', '0002_alter_event_urlsite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='descricao',
            field=models.TextField(null=True),
        ),
    ]
