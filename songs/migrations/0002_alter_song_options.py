# Generated by Django 4.0.7 on 2022-12-16 00:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='song',
            options={'ordering': ('id',)},
        ),
    ]
