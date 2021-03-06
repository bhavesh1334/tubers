# Generated by Django 3.1.7 on 2021-03-12 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('nikon', 'nikon'), ('canon', 'canon'), ('red', 'red'), ('sony', 'sony'), ('fuji', 'fuji'), ('other', 'other')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('mobile_review', 'mobile_review'), ('code', 'code'), ('film_making', 'film_making'), ('comedy', 'comedy'), ('cooking', 'cooking'), ('gaming', 'gaming'), ('vlogs', 'vlogs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('large', 'large'), ('solo', 'solo'), ('small', 'small')], max_length=255),
        ),
    ]
