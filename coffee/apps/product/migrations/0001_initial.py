# Generated by Django 3.2.7 on 2021-09-12 14:42

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
                ('choices', django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=32, verbose_name='Choices'), size=None)),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='Title')),
                ('price', models.FloatField(verbose_name='Price')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('updated_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('options', models.ManyToManyField(related_name='products', to='product.Option', verbose_name='Options')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
    ]