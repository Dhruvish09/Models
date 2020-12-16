# Generated by Django 3.1.4 on 2020-12-16 11:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201216_1711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Group_Name', models.CharField(max_length=50)),
                ('Created_At', models.DateField(auto_now_add=True)),
                ('Updated_At', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('First_Name', models.CharField(max_length=50)),
                ('Created_AT', models.DateField(auto_now_add=True)),
                ('Updated_At', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=1024, verbose_name='Address line')),
                ('Doing_Business_As', models.CharField(max_length=255)),
                ('Created_AT', models.DateField(auto_now_add=True)),
                ('updated_At', models.DateField(auto_now=True)),
                ('Group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.group')),
                ('Provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.provider')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='Providers',
            field=models.ManyToManyField(through='app.GroupLocations', to='app.Provider'),
        ),
    ]