# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20140918_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'blog/featured/%Y/%m/%d/', blank=True),
        ),
    ]
