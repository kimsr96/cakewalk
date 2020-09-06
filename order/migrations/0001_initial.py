# Generated by Django 3.0.3 on 2020-09-05 03:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_store', models.CharField(max_length=25)),
                ('order_product', models.CharField(max_length=25)),
                ('order_number', models.CharField(max_length=20)),
                ('order_cake_img', models.ImageField(upload_to='images/')),
                ('order_price', models.PositiveIntegerField()),
                ('order_date', models.DateField()),
                ('order_pickuptime', models.TimeField()),
                ('order_state', models.CharField(max_length=20)),
                ('order_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_star', models.FloatField()),
                ('review_title', models.CharField(max_length=50)),
                ('review_body', models.TextField()),
                ('review_img', models.ImageField(upload_to='images/')),
                ('review_like', models.PositiveIntegerField(default=0)),
                ('review_unlike', models.PositiveIntegerField(default=0)),
                ('review_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='order.Order')),
            ],
        ),
    ]
