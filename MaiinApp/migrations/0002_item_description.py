# Generated by Django 5.0 on 2023-12-15 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MaiinApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(default='Какое-то описание', max_length=1000),
        ),
    ]