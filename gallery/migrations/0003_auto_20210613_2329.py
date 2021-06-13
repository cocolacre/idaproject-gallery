# Generated by Django 3.2.4 on 2021-06-13 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_auto_20210613_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='url',
            field=models.CharField(default='https://upload.wikimedia.org/wikipedia/en/7/7d/Lenna_%28test_image%29.png', max_length=1024),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(default='placeholder_name.png', max_length=512, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='resizedimage',
            name='image',
            field=models.ImageField(default='resized_placeholder_name.png', max_length=512, upload_to='resized_uploads/'),
        ),
        migrations.AlterField(
            model_name='resizedimage',
            name='original',
            field=models.ForeignKey(default='placeholder_name.png', on_delete=django.db.models.deletion.CASCADE, to='gallery.image'),
        ),
    ]
