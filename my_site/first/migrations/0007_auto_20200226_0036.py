# Generated by Django 3.0.3 on 2020-02-25 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20200225_0042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
