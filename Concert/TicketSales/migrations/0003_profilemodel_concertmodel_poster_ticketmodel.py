# Generated by Django 5.2 on 2025-04-05 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TicketSales', '0002_alter_locationmodel_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Family', models.CharField(max_length=100)),
                ('ProfileImage', models.ImageField(upload_to='ProfileImages/')),
                ('Gender', models.IntegerField(choices=[('Man', 'Man'), ('Woman', 'Woman')])),
            ],
        ),
        migrations.AddField(
            model_name='concertmodel',
            name='Poster',
            field=models.ImageField(null=True, upload_to='ConcertImages/'),
        ),
        migrations.CreateModel(
            name='TicketModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Price', models.IntegerField()),
                ('TicketImage', models.ImageField(upload_to='TicketImages/')),
                ('ProfileModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TicketSales.profilemodel')),
                ('TimeModel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='TicketSales.timemodel')),
            ],
        ),
    ]
