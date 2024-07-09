# Generated by Django 4.2.5 on 2024-07-09 00:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('entidades', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='curso',
            options={'ordering': ['comision']},
        ),
        migrations.AlterModelOptions(
            name='profesor',
            options={'ordering': ['nombre', 'apellido'], 'verbose_name': 'Profesor', 'verbose_name_plural': 'Profesores'},
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
