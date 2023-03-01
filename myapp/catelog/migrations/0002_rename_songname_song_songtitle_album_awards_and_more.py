# Generated by Django 4.1.7 on 2023-03-01 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catelog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='songName',
            new_name='songTitle',
        ),
        migrations.AddField(
            model_name='album',
            name='awards',
            field=models.ManyToManyField(related_name='albums', to='catelog.awards'),
        ),
        migrations.AddField(
            model_name='album',
            name='songs',
            field=models.ManyToManyField(related_name='albums', to='catelog.song'),
        ),
    ]
