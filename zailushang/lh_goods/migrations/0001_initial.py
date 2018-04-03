# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('gtitle', models.CharField(max_length=20)),
                ('gpic', models.ImageField(upload_to='lh_goods')),
                ('gprice', models.DecimalField(decimal_places=2, max_digits=7)),
                ('isDelete', models.BooleanField(default=False)),
                ('gunit', models.CharField(default='人', max_length=20)),
                ('gclick', models.IntegerField()),
                ('gbrief', models.CharField(max_length=300)),
                ('gstock', models.IntegerField()),
                ('gdetails', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ttitle', models.CharField(max_length=20)),
                ('isDelete', models.BooleanField(default=False)),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ForeignKey(to='lh_goods.TypeInfo'),
        ),
    ]
