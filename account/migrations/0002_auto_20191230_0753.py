# Generated by Django 3.0.1 on 2019-12-30 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('space', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='space.Spaces')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.Accounts')),
            ],
            options={
                'db_table': 'likes',
            },
        ),
        migrations.AddField(
            model_name='accounts',
            name='like',
            field=models.ManyToManyField(through='account.Likes', to='space.Spaces'),
        ),
    ]
