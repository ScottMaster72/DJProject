# Generated by Django 3.2.5 on 2022-06-12 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Changarro', '0003_registro'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proovedores',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Empresa', models.CharField(max_length=100, verbose_name='Empresa:')),
                ('Telefono', models.CharField(max_length=100, verbose_name='Telefono:')),
                ('Orden', models.CharField(max_length=100, verbose_name='Orden:')),
                ('Entregado', models.CharField(max_length=50, verbose_name='Entregado:')),
            ],
        ),
    ]