# Generated by Django 4.0.6 on 2022-08-05 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('generator', '0002_alter_profile_generated_icons'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='generated_icons',
            field=models.ManyToManyField(blank=True, to='generator.favicons'),
        ),
    ]
