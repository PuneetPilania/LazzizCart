# Generated by Django 2.2.3 on 2019-07-12 13:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190712_1742'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='chead1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='chead2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head1',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='head2',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='pub_date',
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='thumbnail',
        ),
    ]
