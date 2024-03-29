# Generated by Django 4.2.8 on 2023-12-26 16:20

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cook_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='directions',
            field=ckeditor.fields.RichTextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='ingredients',
            field=ckeditor.fields.RichTextField(default=34),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='prep_time',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Recipe',
        ),
    ]
