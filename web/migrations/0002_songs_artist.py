# Generated by Django 2.1.5 on 2019-02-28 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='songs',
            name='artist',
            field=models.CharField(default='artist', max_length=100),
        ),
    ]
