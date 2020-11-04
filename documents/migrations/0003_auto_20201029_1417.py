# Generated by Django 3.1.2 on 2020-10-29 08:47

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('documents', '0002_auto_20201025_1118'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='tags',
        ),
        migrations.AddField(
            model_name='document',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]