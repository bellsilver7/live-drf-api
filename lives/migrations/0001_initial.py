# Generated by Django 4.2 on 2023-04-11 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('short_description', models.TextField()),
                ('profile_image', models.ImageField(null=True, upload_to='lives/host')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=100, null=True)),
                ('thumbnail', models.ImageField(null=True, upload_to='lives/program')),
                ('stream_status', models.CharField(choices=[('live', 'Live'), ('upcoming', 'Upcoming'), ('finished', 'Finished')], default='upcoming', max_length=100)),
                ('stream_scheduled_at', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('hosts', models.ManyToManyField(blank=True, to='lives.host', verbose_name='호스트 목록')),
            ],
        ),
    ]
