# Generated by Django 3.0.8 on 2020-10-31 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20201031_2219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantimagefile',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
    ]
