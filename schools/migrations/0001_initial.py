# Generated by Django 4.1.2 on 2022-10-28 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(choices=[(None, 'Your String For Display')], max_length=100)),
                ('last_name', models.CharField(choices=[(None, 'Your String For Display')], max_length=100)),
                ('mark', models.CharField(choices=[('1', 'Good'), ('2', 'Very Good')], max_length=50)),
            ],
        ),
    ]