# Generated by Django 3.2.2 on 2021-05-15 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Password',
            field=models.TextField(),
        ),
    ]