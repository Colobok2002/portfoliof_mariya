# Generated by Django 4.1.7 on 2023-03-28 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0002_alter_for_me_name_alter_for_me_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_me',
            name='photo',
            field=models.ImageField(blank=True, upload_to='For_me/40', verbose_name='Обложка'),
        ),
    ]
