# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-13 15:43
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DBMS_catalog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dbms_name', models.TextField()),
                ('version', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Knob_catalog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dbms_id', models.IntegerField()),
                ('name', models.TextField()),
                ('vartype', models.TextField()),
                ('unit', models.TextField(null=True)),
                ('category', models.TextField(null=True)),
                ('summary', models.TextField(null=True)),
                ('description', models.TextField(null=True)),
                ('scope', models.TextField()),
                ('dynamic', models.BooleanField()),
                ('min_value', models.TextField(null=True)),
                ('max_value', models.TextField(null=True)),
                ('valid_vals', models.TextField(null=True)),
                ('default_val', models.TextField()),
                ('deprecated', models.BooleanField()),
                ('dangerous', models.TextField(null=True)),
                ('safe_vals', models.TextField(null=True)),
                ('rank', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='KNOB_PARAMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('db_type', models.CharField(max_length=64)),
                ('params', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Metric_catalog',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('dbms_id', models.IntegerField()),
                ('scale', models.TextField()),
                ('name', models.TextField()),
                ('vartype', models.TextField()),
                ('description', models.TextField(null=True)),
                ('scope', models.TextField(null=True)),
                ('featured', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Oltpbench_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dbms_name', models.CharField(max_length=64)),
                ('dbms_version', models.CharField(max_length=64)),
                ('hardware', models.CharField(max_length=64, null=True)),
                ('cluster', models.TextField(null=True)),
                ('summary', models.TextField()),
                ('res', models.TextField()),
                ('status', models.TextField()),
                ('cfg', models.TextField()),
                ('raw', models.TextField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Workload_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isolation', models.CharField(max_length=64)),
                ('scalefactor', models.IntegerField()),
                ('terminals', models.IntegerField()),
                ('time', models.IntegerField()),
                ('rate', models.CharField(max_length=64)),
                ('skew', models.FloatField(null=True)),
                ('trans_weights', models.TextField()),
                ('workload', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='result',
            name='most_similar',
            field=models.CommaSeparatedIntegerField(max_length=100),
        ),
        migrations.AddField(
            model_name='oltpbench_info',
            name='wid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='website.Workload_info'),
        ),
    ]
