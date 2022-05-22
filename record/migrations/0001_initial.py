# Generated by Django 3.2 on 2021-12-19 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SectionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='浏览时间')),
                ('is_collect', models.BooleanField(default=False, verbose_name='是否收藏')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.section', verbose_name='笔记标题')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '笔记浏览记录',
                'verbose_name_plural': '笔记浏览记录',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='SectionComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('like', models.IntegerField(default=0, verbose_name='评论点赞数')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='record.sectioncomment', verbose_name='父评论')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.section', verbose_name='笔记')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '笔记评论回复记录',
                'verbose_name_plural': '笔记评论回复记录',
                'ordering': ('-time', 'section'),
            },
        ),
        migrations.CreateModel(
            name='LeaveMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='留言内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='留言时间')),
                ('like', models.IntegerField(default=0, verbose_name='留言点赞数')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='record.leavemessage', verbose_name='父留言')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '留言回复记录',
                'verbose_name_plural': '留言回复记录',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='ArticleHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='浏览时间')),
                ('is_collect', models.BooleanField(default=False, verbose_name='是否收藏')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='文章名')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '文章浏览记录',
                'verbose_name_plural': '文章浏览记录',
                'ordering': ('-time',),
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='评论内容')),
                ('time', models.DateTimeField(auto_now_add=True, verbose_name='评论时间')),
                ('like', models.IntegerField(default=0, verbose_name='评论点赞数')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='文章')),
                ('father', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sub', to='record.articlecomment', verbose_name='父评论')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='用户名')),
            ],
            options={
                'verbose_name': '文章评论回复记录',
                'verbose_name_plural': '文章评论回复记录',
                'ordering': ('-time', 'article'),
            },
        ),
    ]