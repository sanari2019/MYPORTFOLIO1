# Generated by Django 4.2 on 2023-04-27 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyPortfolioApp', '0005_remove_portfolio_slug_portfolio_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('document', models.FileField(upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
