# Generated by Django 4.0.1 on 2022-01-31 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_rename_article_review_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='news',
            new_name='new',
        ),
    ]
