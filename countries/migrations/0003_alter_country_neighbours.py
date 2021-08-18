# Generated by Django 3.2.6 on 2021-08-18 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_auto_20210817_1633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='neighbours',
            field=models.ManyToManyField(blank=True, related_name='countries', to='countries.Neighbour'),
        ),
    ]