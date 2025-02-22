# Generated by Django 4.2.19 on 2025-02-12 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_choirmember_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['first_name', 'last_name']},
        ),
        migrations.AddField(
            model_name='customuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
        migrations.AddField(
            model_name='customuser',
            name='voice_part',
            field=models.CharField(blank=True, choices=[('soprano', 'Soprano'), ('alto', 'Alto'), ('tenor', 'Tenor'), ('bass', 'Bass')], max_length=10, null=True),
        ),
    ]
