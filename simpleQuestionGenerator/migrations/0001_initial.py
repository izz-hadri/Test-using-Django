# Generated by Django 3.2.6 on 2021-08-06 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creatorUsername', models.CharField(max_length=200)),
                ('creatorEmail', models.CharField(max_length=200)),
                ('creatorName', models.CharField(max_length=200)),
                ('creatorAge', models.CharField(max_length=3)),
                ('creatorOccupation', models.CharField(max_length=200)),
            ],
        ),
    ]