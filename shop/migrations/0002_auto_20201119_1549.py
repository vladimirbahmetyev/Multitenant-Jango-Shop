# Generated by Django 3.1.3 on 2020-11-19 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='picture',
            field=models.CharField(default='', max_length=500000),
        ),
        migrations.AlterField(
            model_name='usertenant',
            name='token',
            field=models.TextField(default=''),
        ),
    ]