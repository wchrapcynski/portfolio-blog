# Generated by Django 3.0.5 on 2020-04-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_post_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
