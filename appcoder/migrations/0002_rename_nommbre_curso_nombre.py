# Generated by Django 5.1.2 on 2024-12-02 21:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appcoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='nommbre',
            new_name='nombre',
        ),
    ]