# Generated by Django 4.0.6 on 2022-07-14 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0009_perfil'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='image',
            field=models.ImageField(default='perfil.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='perfil.png', upload_to=''),
        ),
    ]