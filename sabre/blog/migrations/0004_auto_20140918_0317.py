# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_entry_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='featured_image',
            field=models.ImageField(null=True, upload_to=b'blog/uploads/featured/%Y/%m/%d/', blank=True),
        ),
    ]
