# Generated by Django 3.2.5 on 2022-06-12 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Changarro', '0002_auto_20220611_1612'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, verbose_name='Nombre:')),
                ('telefono', models.CharField(max_length=10, verbose_name='Telefono:')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo Electronico:')),
                ('contraseña', models.CharField(max_length=100, verbose_name='Contraseña:')),
            ],
        ),
    ]
