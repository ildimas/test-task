# Generated by Django 4.1.2 on 2023-08-11 12:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_category_alter_shop_imageurl'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shop',
            old_name='imageUrl',
            new_name='image',
        ),
    ]
