# Generated by Django 3.1.6 on 2021-02-07 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=60)),
                ('age', models.IntegerField(max_length=5)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=10)),
                ('unit', models.IntegerField(max_length=10)),
                ('date', models.IntegerField(max_length=40)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contact', models.CharField(max_length=10)),
                ('emailid', models.CharField(max_length=60)),
                ('age', models.IntegerField(max_length=5)),
                ('gender', models.CharField(max_length=10)),
                ('plan', models.CharField(max_length=10)),
                ('joindate', models.IntegerField(max_length=10)),
                ('expiredate', models.IntegerField(max_length=10)),
                ('initalamount', models.IntegerField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('amount', models.IntegerField(max_length=10)),
                ('duraton', models.CharField(max_length=20)),
            ],
        ),
    ]
