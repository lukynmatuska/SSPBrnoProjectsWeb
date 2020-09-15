# Generated by Django 3.1.1 on 2020-09-14 15:13

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=30)),
                ('text', models.TextField(default='', max_length=3000)),
                ('users', models.TextField(null=True)),
                ('date_from', models.CharField(default='', max_length=100)),
                ('date_to', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=30)),
                ('password', models.CharField(default='', max_length=300)),
                ('email', models.EmailField(default='', max_length=254)),
                ('icon', models.CharField(default='image/user_default/user.png', max_length=300)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answers', models.CharField(max_length=300)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.event')),
            ],
        ),
        migrations.CreateModel(
            name='Study_material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('path', models.CharField(max_length=300)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.event')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(max_length=300)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='creator',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.user'),
        ),
        migrations.CreateModel(
            name='Completed_survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.TextField(null=True)),
                ('question', models.CharField(max_length=300)),
                ('answers', models.CharField(max_length=300)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.event')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='', max_length=300)),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.event')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
        migrations.CreateModel(
            name='Anketa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('points', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('event', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.event')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.user')),
            ],
        ),
    ]
