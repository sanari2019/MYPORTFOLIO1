# Generated by Django 4.0.1 on 2022-10-19 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolioApp', '0002_alter_skill_skill_set1_alter_skill_skill_set2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='portfolio',
            name='slug',
            field=models.SlugField(default='HI', unique=True),
        ),
    ]
