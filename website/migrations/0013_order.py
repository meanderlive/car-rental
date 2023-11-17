# Generated by Django 3.0.5 on 2020-07-30 11:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_customer_profilepic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.CharField(max_length=10, null=True)),
                ('startRent', models.DateTimeField(null=True)),
                ('endRent', models.DateTimeField(null=True)),
                ('orderDate', models.DateTimeField(auto_now_add=True, null=True)),
                ('pickUpPlace', models.CharField(choices=[('Podwale 11 Lublin', 'Podwale 11 Lublin'), ('2145 Sunset Blvd', '2145 Sunset Blvd'), ('221b Baker St. London', '221b Baker St. London')], max_length=105, null=True)),
                ('fullFuel', models.BooleanField(blank=True, null=True)),
                ('carModel', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Car')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.Customer')),
            ],
        ),
    ]