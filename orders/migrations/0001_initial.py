# Generated by Django 4.2.3 on 2023-07-14 10:09

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
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_status', models.CharField(choices=[('PENDING', 'Pending'), ('IN_TRANSIT', 'In_Transit'), ('DELIVERED', 'delivered')], default='PENDING', max_length=25)),
                ('size', models.CharField(choices=[('SMALL', 'Small'), ('MEDIUM', 'Medium'), ('LARGE', 'Large'), ('EXTRA_LARGE', 'Extra_Large')], default='SMALL', max_length=25)),
                ('quantity', models.IntegerField()),
                ('flavour', models.CharField(max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
