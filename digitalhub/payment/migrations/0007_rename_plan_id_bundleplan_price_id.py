# Generated by Django 5.0.6 on 2024-09-01 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_rename_plan_id_standaloneplan_price_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bundleplan',
            old_name='plan_id',
            new_name='price_id',
        ),
    ]
