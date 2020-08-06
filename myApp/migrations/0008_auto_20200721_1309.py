# Generated by Django 3.0.8 on 2020-07-21 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0007_auto_20200719_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='branchers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myApp.Course'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='contacts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contact', to='myApp.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myApp.Category'),
        ),
    ]