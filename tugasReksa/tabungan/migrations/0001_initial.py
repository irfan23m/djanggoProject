# Generated by Django 2.2.7 on 2019-11-11 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userName', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fullName', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('dateReg', models.DateField()),
                ('exp', models.FloatField()),
                ('level', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='ReksaDana',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('unitNumber', models.FloatField()),
                ('userName', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tabungan.User')),
            ],
        ),
    ]
