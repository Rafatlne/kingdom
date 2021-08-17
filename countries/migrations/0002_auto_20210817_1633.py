# Generated by Django 3.2.6 on 2021-08-17 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='country',
            old_name='alpha2Code',
            new_name='alpha2code',
        ),
        migrations.RenameField(
            model_name='neighbour',
            old_name='alpha3Code',
            new_name='alpha3code',
        ),
        migrations.RemoveField(
            model_name='language',
            name='countries',
        ),
        migrations.RemoveField(
            model_name='neighbour',
            name='countries',
        ),
        migrations.AddField(
            model_name='country',
            name='languages',
            field=models.ManyToManyField(related_name='countries', to='countries.Language'),
        ),
        migrations.AddField(
            model_name='country',
            name='neighbours',
            field=models.ManyToManyField(related_name='countries', to='countries.Neighbour'),
        ),
        migrations.AlterField(
            model_name='country',
            name='flag',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='country',
            name='population',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='country',
            name='timezone',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]
