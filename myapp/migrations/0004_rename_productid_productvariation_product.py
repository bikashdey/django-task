# Generated by Django 3.2.4 on 2021-07-01 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_auto_20210701_2035'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productvariation',
            old_name='productid',
            new_name='product',
        ),
    ]