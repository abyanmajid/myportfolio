# Generated by Django 4.0.6 on 2022-07-24 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_remove_image_name_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, upload_to='myportfolio/main/static/main/assets/img/portfolio'),
        ),
    ]
