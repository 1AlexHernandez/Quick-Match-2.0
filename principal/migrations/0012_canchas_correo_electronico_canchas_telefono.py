# Generated by Django 4.0.6 on 2022-07-26 22:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0011_alter_perfil_image_alter_profile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='canchas',
            name='correo_electronico',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='canchas',
            name='telefono',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]