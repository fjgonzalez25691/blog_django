# Generated by Django 4.1.7 on 2023-04-16 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('entrada', '0001_initial'),
        ('favoritos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='favorites',
            name='entry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entry_favorites', to='entrada.entry'),
        ),
    ]
