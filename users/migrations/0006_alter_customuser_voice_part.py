# Generated by Django 4.2.19 on 2025-02-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_customuser_options_customuser_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='voice_part',
            field=models.CharField(blank=True, choices=[('T1', 'Tenor 1'), ('T2', 'Tenor 2'), ('B1', 'Bass 1'), ('B2', 'Bass 2')], max_length=2, null=True),
        ),
    ]
