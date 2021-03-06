# Generated by Django 3.0.2 on 2020-01-10 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField(choices=[(1, 'Doo-doo'), (2, 'Reggie Miller'), (3, 'Decent'), (4, 'Bomb'), (5, 'GOAT')])),
                ('flower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Flower')),
                ('grower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.Grower')),
            ],
        ),
    ]
