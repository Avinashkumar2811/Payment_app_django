# Generated by Django 5.0.6 on 2024-06-30 11:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('MR', 'Mobile Recharge'), ('DR', 'DTH Recharge'), ('IP', 'Insurance Payment')], max_length=2, unique=True)),
                ('mode_of_payment', models.CharField(choices=[('UPI', 'UPI'), ('IB', 'Internet Banking'), ('CP', 'Card Payment')], max_length=3)),
                ('company', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ServiceUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('age', models.PositiveIntegerField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('transaction_id', models.CharField(max_length=20, unique=True)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.service')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subscriptions.serviceuser')),
            ],
        ),
    ]
