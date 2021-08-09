# Generated by Django 3.2.6 on 2021-08-07 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleQuestionGenerator', '0002_remove_creator_creatoroccupation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planName', models.CharField(blank=True, choices=[('1', 'Standard'), ('2', 'Premium')], max_length=100, null=True)),
                ('planPrice', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='creator',
            name='creatorOccupation',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='creatorAge',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='creatorEmail',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='creatorName',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='creator',
            name='creatorUsername',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
