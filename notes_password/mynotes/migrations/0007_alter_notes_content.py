# Generated by Django 3.2.9 on 2022-06-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mynotes', '0006_alter_notes_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(max_length=10000),
        ),
    ]
