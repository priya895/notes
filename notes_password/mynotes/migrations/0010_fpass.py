# Generated by Django 3.2.9 on 2022-06-13 16:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0009_rename_user_notes_owner'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fpass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ftitle', models.CharField(max_length=64)),
                ('fpass', models.CharField(max_length=64)),
                ('Fwish', models.BooleanField(default=False)),
                ('fuser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fuser', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
