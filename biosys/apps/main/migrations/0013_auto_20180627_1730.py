# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-27 09:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0012_auto_20180611_1558'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a name for the program (required).', max_length=300, unique=True, verbose_name='Name')),
                ('code', models.CharField(blank=True, help_text='Provide a brief code or acronym for this program.', max_length=30, null=True, verbose_name='Code')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
                ('data_engineers', models.ManyToManyField(blank=True, help_text='Users that can create/update projects and dataset schema within this program.', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name_plural': 'media'},
        ),
        migrations.AddField(
            model_name='project',
            name='program',
            field=models.ForeignKey(blank=True, help_text='The program this project belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, to='main.Program'),
        ),
    ]
