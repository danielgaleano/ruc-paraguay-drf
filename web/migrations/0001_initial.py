# Generated by Django 3.2.18 on 2023-03-07 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ruc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=32, verbose_name='Nro. de RUC')),
                ('nombre', models.CharField(max_length=512, verbose_name='Nombre o Denominacion')),
                ('dv', models.CharField(max_length=1, verbose_name='Digito verificador')),
                ('numero_anterior', models.CharField(max_length=32, verbose_name='Nro anterior')),
                ('estado', models.CharField(max_length=32, verbose_name='Estado')),
            ],
        ),
    ]
