# Generated by Django 4.0.6 on 2022-07-11 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0003_alter_profile_image_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='descripcion',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='perfil.jfif', upload_to=''),
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
