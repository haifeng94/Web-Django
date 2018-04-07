# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lh_goods', '0001_initial'),
        ('lh_user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CartInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('ucount', models.IntegerField()),
                ('goods', models.ForeignKey(to='lh_goods.GoodsInfo')),
                ('user', models.ForeignKey(to='lh_user.UserInfo')),
            ],
        ),
    ]
