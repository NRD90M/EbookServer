# Generated by Django 2.0.1 on 2019-05-04 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='time',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
