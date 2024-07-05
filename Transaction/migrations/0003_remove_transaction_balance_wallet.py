# Generated by Django 4.2.13 on 2024-07-04 05:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Transaction', '0002_alter_transaction_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='balance',
        ),
        migrations.CreateModel(
            name='wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=100000, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
