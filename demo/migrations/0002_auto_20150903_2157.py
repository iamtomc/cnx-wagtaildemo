# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import wagtail.wagtailimages.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailcore.blocks
import wagtail.wagtailembeds.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homepage',
            options={},
        ),
        migrations.AlterField(
            model_name='contactpage',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='choices',
            field=models.CharField(help_text='Comma separated list of choices. Only applicable in checkboxes, radio and dropdown.', max_length=512, verbose_name='Choices', blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='default_value',
            field=models.CharField(help_text='Default value. Comma separated values supported for checkboxes.', max_length=255, verbose_name='Default value', blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='field_type',
            field=models.CharField(max_length=16, verbose_name='Field type', choices=[('singleline', 'Single line text'), ('multiline', 'Multi-line text'), ('email', 'Email'), ('number', 'Number'), ('url', 'URL'), ('checkbox', 'Checkbox'), ('checkboxes', 'Checkboxes'), ('dropdown', 'Drop down'), ('radio', 'Radio buttons'), ('date', 'Date'), ('datetime', 'Date/time')]),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='help_text',
            field=models.CharField(max_length=255, verbose_name='Help text', blank=True),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='label',
            field=models.CharField(help_text='The label of the form field', max_length=255, verbose_name='Label'),
        ),
        migrations.AlterField(
            model_name='formfield',
            name='required',
            field=models.BooleanField(default=True, verbose_name='Required'),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='from_address',
            field=models.CharField(max_length=255, verbose_name='From address', blank=True),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='subject',
            field=models.CharField(max_length=255, verbose_name='Subject', blank=True),
        ),
        migrations.AlterField(
            model_name='formpage',
            name='to_address',
            field=models.CharField(help_text='Optional - form submissions will be emailed to this address', max_length=255, verbose_name='To address', blank=True),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField([(b'heading', wagtail.wagtailcore.blocks.CharBlock(classname=b'full title')), (b'paragraph', wagtail.wagtailcore.blocks.RichTextBlock()), (b'image', wagtail.wagtailimages.blocks.ImageChooserBlock()), (b'embeded_content', wagtail.wagtailembeds.blocks.EmbedBlock()), (b'raw_HTML', wagtail.wagtailcore.blocks.RawHTMLBlock())]),
        ),
        migrations.AlterField(
            model_name='personpage',
            name='email',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
