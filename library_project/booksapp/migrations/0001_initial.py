# Generated by Django 5.1.4 on 2024-12-20 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=100)),
                ('Year', models.IntegerField()),
                ('Genre', models.CharField(max_length=100)),
            ],
        ),
    ]
