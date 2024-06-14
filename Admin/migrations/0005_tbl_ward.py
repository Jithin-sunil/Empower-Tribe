# Generated by Django 5.0.4 on 2024-04-24 10:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_ward',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ward', models.CharField(max_length=50)),
                ('localbody', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_localbody')),
            ],
        ),
    ]
