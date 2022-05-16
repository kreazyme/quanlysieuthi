# Generated by Django 3.0.14 on 2022-05-16 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Production',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('name', models.TextField()),
                ('producttype', models.TextField()),
                ('price', models.IntegerField(default=0)),
            ],
        ),
    ]