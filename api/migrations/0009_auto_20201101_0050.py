# Generated by Django 3.0.8 on 2020-10-31 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20201101_0029'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='howtogetthere',
            name='post_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='review_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='RestaurantMenuFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, help_text='Restaurant Menu.', null=True, upload_to='restaurant_menu/')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Restaurant')),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
