# Generated by Django 3.1.3 on 2020-11-24 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201123_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='list_items',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_group', models.CharField(max_length=255)),
                ('nmae_item', models.CharField(max_length=255)),
                ('FCs', models.CharField(max_length=255)),
                ('quantity_works', models.IntegerField()),
            ],
        ),
    ]
