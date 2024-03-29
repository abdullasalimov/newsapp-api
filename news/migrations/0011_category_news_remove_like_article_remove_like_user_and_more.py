# Generated by Django 4.0.1 on 2022-04-04 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0010_article_views'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('is_favourite', models.BooleanField(default=False)),
                ('views', models.IntegerField(blank=True, default=0, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.category')),
                ('likes', models.ManyToManyField(blank=True, default=None, related_name='likes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='like',
            name='article',
        ),
        migrations.RemoveField(
            model_name='like',
            name='user',
        ),
        migrations.RemoveField(
            model_name='topic',
            name='collection',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='review',
            name='new',
        ),
        migrations.RenameModel(
            old_name='Collection',
            new_name='Region',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.DeleteModel(
            name='Topic',
        ),
        migrations.AddField(
            model_name='news',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.region'),
        ),
        migrations.AddField(
            model_name='category',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='news.region'),
        ),
        migrations.AddField(
            model_name='review',
            name='news',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='news.news'),
            preserve_default=False,
        ),
    ]
