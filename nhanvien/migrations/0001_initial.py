# Generated by Django 4.0.6 on 2022-07-20 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ThemMoiNV',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ten', models.CharField(max_length=100)),
                ('chucvu', models.CharField(max_length=100)),
                ('namsinh', models.CharField(max_length=100)),
            ],
        ),
    ]
