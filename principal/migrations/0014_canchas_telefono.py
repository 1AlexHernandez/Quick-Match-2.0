# Generated by Django 4.0.6 on 2022-08-02 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0013_delete_cancha_delete_personas_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='canchas',
            name='telefono',
            field=models.BigIntegerField(default=1),
            preserve_default=False,
        ),
    ]
