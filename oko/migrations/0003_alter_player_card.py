# Generated by Django 3.2.5 on 2022-03-21 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('oko', '0002_player'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='card',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='oko.card'),
        ),
    ]