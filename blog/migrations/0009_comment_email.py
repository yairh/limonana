# Generated by Django 3.0.6 on 2020-06-08 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_comment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='email',
            field=models.EmailField(default='somemail@limonana.com', max_length=254),
        ),
    ]
