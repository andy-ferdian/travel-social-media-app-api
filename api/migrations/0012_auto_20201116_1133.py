# Generated by Django 3.0.8 on 2020-11-16 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20201115_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantimagefile',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
        migrations.AlterField(
            model_name='restaurantmenufile',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant'),
        ),
    ]
