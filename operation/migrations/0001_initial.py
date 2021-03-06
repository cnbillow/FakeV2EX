# Generated by Django 2.0.2 on 2018-03-03 12:20

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('topic', '0016_auto_20180303_1220'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TopicVote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vote', models.IntegerField(blank=True, choices=[(-1, 'None'), (0, 'False'), (1, 'True')], null=True, verbose_name='是否喜欢此贴')),
                ('thanks', models.IntegerField(blank=True, choices=[(-1, 'None'), (0, 'False'), (1, 'True')], null=True, verbose_name='是否感谢此贴')),
                ('favorite', models.IntegerField(blank=True, choices=[(-1, 'None'), (0, 'False'), (1, 'True')], null=True, verbose_name='是否收藏此贴')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='topic.Topic', verbose_name='Topic')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
            options={
                'verbose_name': 'Topic和用户关联表',
                'verbose_name_plural': 'Topic和用户关联表',
            },
        ),
    ]
