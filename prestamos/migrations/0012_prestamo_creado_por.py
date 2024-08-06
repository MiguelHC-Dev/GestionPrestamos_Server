# Generated by Django 4.2.13 on 2024-08-05 18:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('prestamos', '0011_alter_prestamo_fecha_primer_pago'),
    ]

    operations = [
        migrations.AddField(
            model_name='prestamo',
            name='creado_por',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
