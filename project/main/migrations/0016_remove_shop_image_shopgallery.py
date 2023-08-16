# Generated by Django 4.2.4 on 2023-08-15 09:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_remove_product_images_alter_product_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='image',
        ),
        migrations.CreateModel(
            name='ShopGallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='shop_pictures')),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shops', to='main.shop')),
            ],
        ),
    ]
