# Generated by Django 2.1.5 on 2019-02-28 11:20

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)])),
            ],
            options={
                'verbose_name_plural': 'Ratings',
            },
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=100)),
                ('song_img', models.FileField(upload_to='')),
            ],
            options={
                'verbose_name_plural': 'Songs',
            },
        ),
        migrations.AddField(
            model_name='ratings',
            name='song',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Songs'),
        ),
        migrations.AddField(
            model_name='ratings',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]