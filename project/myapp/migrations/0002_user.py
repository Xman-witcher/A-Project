# Generated by Django 4.1.5 on 2023-03-15 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('app', models.CharField(max_length=100)),
                ('points', models.IntegerField()),
            ],
        ),
    ]
