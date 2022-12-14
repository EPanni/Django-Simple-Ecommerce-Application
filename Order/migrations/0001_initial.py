# Generated by Django 4.0.6 on 2022-08-03 15:43

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
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.FloatField()),
                ('status', models.CharField(choices=[('A', 'Approved'), ('C', 'Created'), ('R', 'Reproved'), ('P', 'Pendent'), ('S', 'Sent'), ('F', 'Finishes')], default='C', max_length=1)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=255)),
                ('producti_id', models.PositiveBigIntegerField()),
                ('variation', models.CharField(max_length=255)),
                ('variation_id', models.PositiveIntegerField()),
                ('price', models.FloatField()),
                ('price_promo', models.FloatField(default=0)),
                ('amount', models.PositiveIntegerField()),
                ('image', models.CharField(max_length=2000)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Order.order')),
            ],
            options={
                'verbose_name': "Order's item ",
                'verbose_name_plural': "Order's items ",
            },
        ),
    ]
