# Generated by Django 4.1.1 on 2022-10-25 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pic')),
                ('year', models.IntegerField()),
                ('desc', models.TextField()),
            ],
        ),
    ]
