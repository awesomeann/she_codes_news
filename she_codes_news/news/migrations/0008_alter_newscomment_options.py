# Generated by Django 4.2.2 on 2023-12-06 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0007_alter_newscategory_name_newscomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newscomment',
            options={'ordering': ['date']},
        ),
    ]