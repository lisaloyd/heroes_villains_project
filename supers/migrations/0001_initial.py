# Generated by Django 4.1.5 on 2023-01-10 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Super',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('alter_ego', models.CharField(max_length=255)),
                ('primary_ability', models.CharField(max_length=255)),
                ('secondary_ability', models.CharField(max_length=255)),
                ('catchphrase', models.CharField(max_length=255)),
                ('super_type', models.CharField(max_length=255)),
            ],
        ),
    ]
