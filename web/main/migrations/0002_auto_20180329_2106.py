# Generated by Django 2.0.3 on 2018-03-29 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.ImageField(default='/media/image/user_deafult/user.png', upload_to=''),
        ),
    ]