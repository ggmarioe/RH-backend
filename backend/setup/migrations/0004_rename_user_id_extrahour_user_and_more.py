# Generated by Django 4.0.2 on 2022-03-02 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('setup', '0003_rename_user_extrahour_user_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrahour',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='extrahourhistory',
            old_name='user_id',
            new_name='user',
        ),
    ]