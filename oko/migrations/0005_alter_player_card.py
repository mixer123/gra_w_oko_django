# Generated by Django 3.2.5 on 2022-03-21 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oko', '0004_card_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='oko.card'),
        ),
    ]
