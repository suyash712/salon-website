# Generated by Django 4.2.3 on 2024-09-21 12:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='salon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salon_name', models.CharField(max_length=200)),
                ('location', models.CharField(max_length=200)),
                ('address', models.CharField(default='xyz', max_length=200)),
                ('ratings', models.IntegerField(default=1)),
                ('description', models.CharField(max_length=200)),
                ('reviews', models.CharField(max_length=200)),
                ('image', models.ImageField(upload_to='salon_images/')),
                ('no_of_barbers', models.IntegerField()),
                ('no_of_chairs', models.IntegerField()),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='salon_head',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=200)),
                ('date_of_birth', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('duration', models.IntegerField()),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='salon.salon')),
            ],
        ),
        migrations.AddField(
            model_name='salon',
            name='salon_head',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salon', to='salon.salon_head'),
        ),
    ]
