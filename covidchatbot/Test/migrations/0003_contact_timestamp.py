# Generated by Django 2.2.11 on 2020-05-26 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Test', '0002_auto_20200526_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default='2000-01-01'),
            preserve_default=False,
        ),
    ]