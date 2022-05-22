# Generated by Django 3.2 on 2021-12-25 12:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_delete_useroauth'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthId',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=100, verbose_name='用户OAuthID')),
                ('source', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.usersource', verbose_name='用户来源')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户ID')),
            ],
            options={
                'verbose_name': '第三方登录用户ID',
                'verbose_name_plural': '第三方登录用户ID',
            },
        ),
    ]
