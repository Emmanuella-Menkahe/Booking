# Generated by Django 5.1 on 2024-10-02 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_customuser_roles'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agency',
        ),
    ]
