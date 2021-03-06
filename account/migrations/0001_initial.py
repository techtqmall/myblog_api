# Generated by Django 3.2 on 2021-12-19 10:42

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=100, verbose_name='关键词')),
            ],
            options={
                'verbose_name': '搜索关键词',
                'verbose_name_plural': '搜索关键词',
            },
        ),
        migrations.CreateModel(
            name='UserSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='来源')),
            ],
            options={
                'verbose_name': '注册用户来源',
                'verbose_name_plural': '注册用户来源',
            },
        ),
        migrations.CreateModel(
            name='UserOAuth',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=50, verbose_name='key')),
                ('secret', models.CharField(max_length=50, verbose_name='secret')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.usersource', verbose_name='第三方平台名称')),
            ],
            options={
                'verbose_name': '第三方平台密钥',
                'verbose_name_plural': '第三方平台密钥',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.CharField(blank=True, max_length=20, null=True, verbose_name='手机号')),
                ('sex', models.CharField(choices=[('1', '男'), ('2', '女')], default=1, max_length=1, verbose_name='性别')),
                ('web', models.URLField(blank=True, null=True, verbose_name='个人网站')),
                ('signature', models.TextField(default='这个人很懒，什么都没留下！', max_length=200, verbose_name='个性签名')),
                ('photo', models.URLField(default='https://oss.cuiliangblog.cn/images/photo.jpg', verbose_name='头像')),
                ('area_code', models.CharField(blank=True, max_length=10, null=True, verbose_name='地区编号')),
                ('area_name', models.CharField(blank=True, max_length=20, null=True, verbose_name='地区名称')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='生日')),
                ('is_flow', models.BooleanField(default=0, verbose_name='开启更新订阅')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('search', models.ManyToManyField(to='account.SearchKey', verbose_name='搜索记录')),
                ('source', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='account.usersource', verbose_name='用户来源')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '用户详细信息',
                'verbose_name_plural': '用户详细信息',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
