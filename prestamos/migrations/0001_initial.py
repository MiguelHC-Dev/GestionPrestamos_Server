# Generated by Django 4.2.13 on 2024-11-27 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_completo', models.CharField(max_length=255)),
                ('fecha_nacimiento', models.DateField()),
                ('domicilio_actual', models.CharField(max_length=255)),
                ('correo_electronico', models.EmailField(blank=True, max_length=254, null=True)),
                ('numero_telefono', models.CharField(max_length=20)),
                ('foto_identificacion', models.ImageField(blank=True, null=True, upload_to='clientes_identificaciones/')),
                ('clave_elector', models.CharField(max_length=18, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imei', models.CharField(max_length=255)),
                ('equipo_a_adquirir', models.CharField(max_length=255)),
                ('equipo_precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('monto_credito', models.DecimalField(decimal_places=2, max_digits=10)),
                ('plazo_credito', models.IntegerField()),
                ('pago_inicial', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interes', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fecha_inicio', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(default='ACTIVO', max_length=100)),
                ('fecha_primer_pago', models.DateField(blank=True, null=True)),
                ('estatus_pago', models.CharField(blank=True, choices=[('A Tiempo', 'A Tiempo'), ('Atrasado', 'Atrasado')], default='A Tiempo', max_length=10, null=True)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.cliente')),
                ('creado_por', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_pago_programada', models.DateField()),
                ('monto_pago', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pagado', models.BooleanField(default=False)),
                ('prestamo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prestamos.prestamo')),
            ],
        ),
    ]
