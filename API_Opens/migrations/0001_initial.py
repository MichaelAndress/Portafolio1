# Generated by Django 4.1 on 2022-11-18 02:29

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
            name='Abogado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_abogado', models.CharField(max_length=200)),
                ('apellido_abogado', models.CharField(max_length=200)),
                ('fono_abogado', models.CharField(max_length=200)),
                ('direccion_abogado', models.CharField(max_length=200)),
                ('email_abogado', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Abogado',
            },
        ),
        migrations.CreateModel(
            name='Bitacora_usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('hora', models.DateTimeField()),
                ('detalle_bitacora', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'Bitacora_usuario',
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('fecha', models.CharField(max_length=200)),
                ('asunto', models.TextField()),
                ('cuerpo', models.TextField()),
            ],
            options={
                'db_table': 'Email',
            },
        ),
        migrations.CreateModel(
            name='Plantilla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('asunto_plantilla', models.TextField()),
                ('cuerpo_plantilla', models.TextField()),
            ],
            options={
                'db_table': 'Plantilla',
            },
        ),
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
                ('fecha', models.DateTimeField()),
                ('prediccion', models.CharField(max_length=200)),
                ('id_abogado', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API_Opens.abogado')),
                ('id_email', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API_Opens.email')),
            ],
            options={
                'db_table': 'Solicitud',
            },
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200, null=True)),
                ('apellido', models.CharField(max_length=200, null=True)),
                ('direccion', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200, null=True)),
                ('fono', models.CharField(max_length=20, null=True)),
                ('fecha_nac', models.DateField(null=True)),
                ('image', models.ImageField(default='foto.png', upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('documento', models.FileField(upload_to='Uploaded Files/')),
                ('fecha_documento', models.DateTimeField(auto_now=True)),
                ('uploadedFile', models.FileField(upload_to='Uploaded Files/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Documento',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cliente', models.CharField(max_length=200)),
                ('apellido_cliente', models.CharField(max_length=200)),
                ('fono_cliente', models.CharField(max_length=200)),
                ('direccion_cliente', models.CharField(max_length=200)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cliente',
            },
        ),
        migrations.CreateModel(
            name='Bitacora_solicitud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_solicitud', models.DateField()),
                ('hora_solicitud', models.DateTimeField()),
                ('detalle_solicitud', models.CharField(max_length=200)),
                ('estado_solicitud', models.CharField(max_length=200)),
                ('id_solicitud', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API_Opens.solicitud')),
            ],
            options={
                'db_table': 'Bitacora_solicitud',
            },
        ),
    ]
