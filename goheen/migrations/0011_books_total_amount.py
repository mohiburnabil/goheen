# Generated by Django 4.0.2 on 2022-04-23 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goheen', '0010_comment_traveller'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='total_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
