# Generated by Django 5.0 on 2024-03-26 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cakes', '0004_alter_cake_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cake',
            name='stars',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
