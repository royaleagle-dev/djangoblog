# Generated by Django 3.1.2 on 2020-10-04 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0003_auto_20201004_1501'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='lBan',
            field=models.ImageField(default='a.jpg', upload_to='uploads/images/l'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='nBan',
            field=models.ImageField(default='b.jpg', upload_to='uploads/images/n'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='pBan',
            field=models.ImageField(default='c.jpg', upload_to='uploads/images/p'),
            preserve_default=False,
        ),
    ]
