# Generated by Django 3.0.3 on 2020-02-24 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_auto_20200225_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
