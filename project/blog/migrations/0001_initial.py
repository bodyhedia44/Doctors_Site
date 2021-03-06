# Generated by Django 3.0.6 on 2020-07-31 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=40)),
                ('image', models.ImageField(upload_to='image_upload')),
                ('time', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('user', models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='author', serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
