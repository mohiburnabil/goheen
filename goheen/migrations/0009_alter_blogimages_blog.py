# Generated by Django 4.0.2 on 2022-04-18 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goheen', '0008_alter_blogimages_blog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogimages',
            name='blog',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='goheen.blog'),
        ),
    ]
