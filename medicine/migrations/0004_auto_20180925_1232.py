# Generated by Django 2.0.5 on 2018-09-25 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicine', '0003_auto_20180924_2008'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicinepacket',
            name='expireing_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='medicinepacket',
            name='manufacturing_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
