# Generated by Django 2.0.3 on 2018-03-29 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20180329_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='image/user_default/user', upload_to=''),
        ),
    ]
