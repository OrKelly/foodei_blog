# Generated by Django 4.2.8 on 2023-12-26 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='photo',
            field=models.ImageField(blank=True, default='users/default.png', null=True, upload_to='users/%Y/%m/%d/', verbose_name='Фотография'),
        ),
    ]
