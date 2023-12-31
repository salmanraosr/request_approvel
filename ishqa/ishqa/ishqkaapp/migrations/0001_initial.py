# Generated by Django 3.2.6 on 2023-11-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Approved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_at', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('mobile', models.IntegerField()),
                ('aadhar', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ishqkaapp.approved')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ishqkaapp.request')),
            ],
        ),
        migrations.AddField(
            model_name='approved',
            name='request',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ishqkaapp.request'),
        ),
    ]
