# Generated by Django 3.1.2 on 2020-11-22 15:02

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('accounts', '0004_auto_20201122_1849'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='important_tags',
        ),
        migrations.AddField(
            model_name='profile',
            name='important_tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
