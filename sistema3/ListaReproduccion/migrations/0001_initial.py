# Generated by Django 4.2.4 on 2023-09-01 20:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('nick', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=45)),
                ('apellido', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=45)),
                ('contraseña', models.CharField(max_length=45)),
            ],
        ),
        migrations.CreateModel(
            name='Cancion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('genero', models.CharField(max_length=20)),
                ('autor', models.CharField(max_length=50)),
                ('titulo', models.CharField(max_length=50)),
                ('usuario_nick', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ListaReproduccion.usuario')),
            ],
        ),
    ]
