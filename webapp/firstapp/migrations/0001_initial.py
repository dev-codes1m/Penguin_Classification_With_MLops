# Generated by Django 4.1.7 on 2023-02-21 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Penguin_Prediction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('island', models.FloatField()),
                ('bill_length_mm', models.FloatField()),
                ('bill_depth_mm', models.FloatField()),
                ('flipper_length_mm', models.FloatField()),
                ('body_mass_g', models.FloatField()),
                ('sex', models.FloatField()),
                ('species', models.FloatField()),
            ],
        ),
    ]