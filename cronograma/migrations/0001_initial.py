# Generated by Django 4.1.5 on 2023-02-04 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Capilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_sede', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Cronograma',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mes_año', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Musico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('contacto', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Misa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('horario', models.CharField(max_length=6)),
                ('responsable', models.CharField(max_length=50)),
                ('observaciones', models.CharField(max_length=150)),
                ('capilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cronograma.capilla')),
                ('cronograma', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cronograma.cronograma')),
                ('musico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cronograma.musico')),
            ],
        ),
    ]
