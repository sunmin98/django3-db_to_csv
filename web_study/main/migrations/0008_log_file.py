# Generated by Django 4.0.5 on 2022-07-19 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_remove_product_category_delete_category_delete_menu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='log_file',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=300)),
                ('class_name', models.CharField(max_length=200)),
                ('percent', models.CharField(max_length=200)),
            ],
        ),
    ]
