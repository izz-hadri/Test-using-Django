# Generated by Django 3.2.6 on 2021-08-07 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('simpleQuestionGenerator', '0005_alter_plan_planname'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='planDescription',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
