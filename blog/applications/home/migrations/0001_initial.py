# Generated by Django 3.0.4 on 2021-02-16 00:36

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('full_name', models.CharField(max_length=60, verbose_name='Nombres')),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Mensajes',
            },
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('title', models.CharField(max_length=30, verbose_name='Alejandro Zúñiga Pérez')),
                ('description', models.TextField()),
                ('about_title', models.CharField(max_length=50, verbose_name='Ingeniería Eléctrica')),
                ('about_text', models.TextField()),
                ('contact_email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail de contacto')),
                ('phone', models.CharField(max_length=15, verbose_name='Teléfono de contacto')),
            ],
            options={
                'verbose_name': 'Pagina Principal',
                'verbose_name_plural': 'Pagina Principal',
            },
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('email', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Suscriptor',
                'verbose_name_plural': 'Suscriptores',
            },
        ),
    ]
