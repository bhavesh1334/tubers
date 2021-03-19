# Generated by Django 3.1.7 on 2021-03-13 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_auto_20210312_1624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('fuji', 'fuji'), ('red', 'red'), ('nikon', 'nikon'), ('other', 'other'), ('sony', 'sony')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('cooking', 'cooking'), ('film_making', 'film_making'), ('vlogs', 'vlogs'), ('gaming', 'gaming'), ('mobile_review', 'mobile_review'), ('code', 'code'), ('comedy', 'comedy')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('large', 'large'), ('small', 'small')], max_length=255),
        ),
    ]
