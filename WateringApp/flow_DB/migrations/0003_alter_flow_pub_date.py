# Generated by Django 3.2.5 on 2021-08-22 14:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('flow_DB', '0002_alter_flow_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flow',
            name='pub_date',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
    ]
