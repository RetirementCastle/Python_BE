# Generated by Django 2.1.2 on 2018-10-04 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nursinghome', models.IntegerField()),
                ('username', models.CharField(default='0', max_length=15)),
                ('password', models.TextField(default='0000000')),
                ('token', models.TextField(default='0')),
            ],
        ),
    ]
