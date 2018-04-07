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
            name='OrderDetailInfo',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('price', models.DecimalField(max_digits=8, decimal_places=2)),
                ('count', models.IntegerField()),
                ('goods', models.ForeignKey(to='lh_goods.GoodsInfo')),
            ],
        ),
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('oid', models.CharField(serialize=False, max_length=20, primary_key=True)),
                ('odate', models.DateTimeField(auto_now=True)),
                ('oIsPay', models.BooleanField(default=False)),
                ('ototal', models.DecimalField(max_digits=8, decimal_places=2)),
                ('oaddress', models.CharField(max_length=150)),
                ('user', models.ForeignKey(to='lh_user.UserInfo')),
            ],
        ),
        migrations.AddField(
            model_name='orderdetailinfo',
            name='order',
            field=models.ForeignKey(to='lh_order.OrderInfo'),
        ),
    ]
