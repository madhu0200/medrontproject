# Generated by Django 4.0.4 on 2022-09-02 16:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_otp_alter_customuser_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='otp',
            old_name='otp',
            new_name='otps',
        ),
    ]
