# Generated by Django 3.0.8 on 2020-07-17 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='type',
            field=models.IntegerField(choices=[(1, 'PHONE'), (2, 'FACEBOOK'), (3, 'EMAIL')]),
        ),
    ]
