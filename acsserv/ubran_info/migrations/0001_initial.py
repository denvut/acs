# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ran_info',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uuid_text', models.CharField(max_length=200)),
                ('ip4_addr', models.GenericIPAddressField(null=True, protocol=b'ipv4', blank=True)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='Ran_ssl',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ssl_key', models.CharField(max_length=200)),
                ('ran_id', models.ForeignKey(to='ubran_info.Ran_info')),
            ],
        ),
    ]
