# Generated by Django 4.2.13 on 2024-06-02 22:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('prestamos', '0005_rename_equipo_imei_prestamo_imei'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prestamo',
            old_name='cliente',
            new_name='cliente_id',
        ),
    ]
