# Generated by Django 3.0.5 on 2020-04-30 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='okta_id',
            field=models.CharField(blank=True, default='0', max_length=20),
        ),
    ]
