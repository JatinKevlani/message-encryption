# Generated by Django 5.0 on 2023-12-29 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('msg_encrypt', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Msgs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('encryption', models.TextField()),
                ('password', models.CharField(max_length=50)),
            ],
        ),
    ]
