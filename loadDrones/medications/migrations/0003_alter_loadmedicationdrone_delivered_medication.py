# Generated by Django 4.0.3 on 2022-03-08 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medications', '0002_alter_medication_load'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loadmedicationdrone',
            name='delivered_medication',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Initial Date'),
        ),
    ]
