# Generated by Django 4.1.7 on 2023-03-28 18:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0006_partners_alter_for_me_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='for_me',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/For_me/64', verbose_name='Обложка'),
        ),
        migrations.AlterField(
            model_name='partners',
            name='photo',
            field=models.ImageField(blank=True, upload_to='image/Partners/59', verbose_name='Обложка'),
        ),
        migrations.CreateModel(
            name='Keys',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200, verbose_name='Название кейса')),
                ('slug', models.SlugField(max_length=200, verbose_name='Уникальный url (Генерируется сам)')),
                ('logo', models.ImageField(blank=True, upload_to='image/products/%Y/%m/%d', verbose_name='Обложка')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('available', models.BooleanField(default=True, verbose_name='Активость')),
            ],
            options={
                'verbose_name': 'Кейсы',
                'verbose_name_plural': 'Кейсы',
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='products/%Y/%m/%d', verbose_name='Дополнительные фото')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='mainsite.keys')),
            ],
        ),
    ]
