# Generated by Django 3.0.8 on 2020-07-19 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0006_auto_20200718_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branchers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='branch', to='myApp.Course'),
        ),
    ]