# Generated by Django 4.0.3 on 2022-03-28 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tranporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dname', models.CharField(default='0000000', max_length=50)),
                ('license_no', models.CharField(default='0000000', max_length=50)),
                ('dphone', models.CharField(default='0000000', max_length=50)),
                ('v_no', models.CharField(default='0000000', max_length=50)),
                ('v_type', models.CharField(default='0000000', max_length=50)),
                ('permit_wt', models.CharField(default='0000000', max_length=50)),
            ],
        ),
    ]