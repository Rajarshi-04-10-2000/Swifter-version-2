# Generated by Django 4.0.3 on 2022-03-28 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstar', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tranporter',
            name='v_status',
            field=models.CharField(default='Available', max_length=50),
        ),
    ]
