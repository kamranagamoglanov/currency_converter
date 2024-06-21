# Generated by Django 5.0.6 on 2024-06-15 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('to_currency', models.CharField(blank=True, max_length=3, null=True)),
                ('amount', models.BigIntegerField()),
            ],
        ),
    ]
