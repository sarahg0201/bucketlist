# Generated by Django 4.1.4 on 2022-12-28 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buckets', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='link',
            field=models.CharField(default='SOME STRING', max_length=500),
        ),
    ]