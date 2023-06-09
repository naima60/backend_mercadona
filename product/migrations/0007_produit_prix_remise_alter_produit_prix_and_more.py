# Generated by Django 4.2 on 2023-05-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_promotion_produit_promotions'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='prix_remise',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='prix',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='taux',
            field=models.FloatField(null=True),
        ),
    ]
