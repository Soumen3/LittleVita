# Generated by Django 5.0.2 on 2024-03-05 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0006_rename_parent_email_parent_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='efficacy',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
