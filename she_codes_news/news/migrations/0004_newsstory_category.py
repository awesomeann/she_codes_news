# Generated by Django 4.2.2 on 2023-12-05 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_newsstory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsstory',
            name='category',
            field=models.CharField(default='default', max_length=40),
            preserve_default=False,
        ),
    ]
