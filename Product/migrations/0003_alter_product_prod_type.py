# Generated by Django 4.0.6 on 2022-08-05 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Product', '0002_variation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_type',
            field=models.CharField(choices=[('V', 'Variable'), ('S', 'Simple')], default='V', max_length=1),
        ),
    ]