# Generated by Django 3.2 on 2021-05-02 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eva_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='urlSite',
            field=models.CharField(max_length=300),
        ),
    ]
