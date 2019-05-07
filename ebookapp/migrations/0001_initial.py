# Generated by Django 2.0.1 on 2019-04-30 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bookideal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('userhead', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('quote', models.TextField()),
                ('likecount', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('username', models.CharField(max_length=20)),
                ('userhead', models.CharField(max_length=100)),
                ('bookidealid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='concern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('concernuser', models.CharField(max_length=10)),
                ('concerneduser', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userid', models.CharField(max_length=10)),
                ('bookidealid', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('sex', models.CharField(max_length=1)),
                ('signature', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=30)),
                ('experience', models.CharField(max_length=100)),
                ('userhead', models.CharField(max_length=100)),
            ],
        ),
    ]
