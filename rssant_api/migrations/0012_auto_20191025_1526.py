# Generated by Django 2.2.6 on 2019-10-25 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rssant_api', '0011_auto_20190714_0550'),
    ]

    operations = [
        migrations.AddField(
            model_name='feed',
            name='monthly_story_count_data',
            field=models.BinaryField(blank=True, help_text='monthly story count data', max_length=514, null=True),
        ),
        migrations.AlterField(
            model_name='feed',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('updating', 'updating'), ('ready', 'ready'), ('error', 'error'), ('discard', 'discard')], default='pending', help_text='状态', max_length=20),
        ),
        migrations.AlterField(
            model_name='feedcreation',
            name='status',
            field=models.CharField(choices=[('pending', 'pending'), ('updating', 'updating'), ('ready', 'ready'), ('error', 'error'), ('discard', 'discard')], default='pending', help_text='状态', max_length=20),
        ),
    ]