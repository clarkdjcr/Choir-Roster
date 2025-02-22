# Generated by Django 5.1.6 on 2025-02-11 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_customuser_created_at_customuser_is_admin'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choirmember',
            options={'ordering': ['last_name', 'first_name']},
        ),
        migrations.AddField(
            model_name='choirmember',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='choirmember',
            name='phone_number',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='choirmember',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='choir_members/'),
        ),
        migrations.AlterField(
            model_name='choirmember',
            name='voice_part',
            field=models.CharField(choices=[('S1', 'Soprano 1'), ('S2', 'Soprano 2'), ('A1', 'Alto 1'), ('A2', 'Alto 2'), ('T1', 'Tenor 1'), ('T2', 'Tenor 2'), ('B1', 'Bass 1'), ('B2', 'Bass 2')], max_length=2),
        ),
    ]
