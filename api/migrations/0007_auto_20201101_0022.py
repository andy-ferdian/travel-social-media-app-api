# Generated by Django 3.0.8 on 2020-10-31 17:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20201031_2318'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviewimagefile',
            name='restaurant',
        ),
        migrations.AddField(
            model_name='reviewimagefile',
            name='review',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='restaurant_review_image', to='api.Review'),
            preserve_default=False,
        ),
    ]
