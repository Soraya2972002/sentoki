# Generated by Django 4.0.4 on 2022-05-27 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voice_messge', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audio_store',
            name='record',
            field=models.ImageField(blank=True, default='media/vocal_test.aac', upload_to=''),
        ),
        migrations.AlterModelTable(
            name='audio_store',
            table=None,
        ),
    ]
