# Generated by Django 4.1.3 on 2022-12-07 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('standup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoughts', models.CharField(max_length=500)),
                ('recommendations', models.CharField(max_length=500)),
            ],
        ),
    ]