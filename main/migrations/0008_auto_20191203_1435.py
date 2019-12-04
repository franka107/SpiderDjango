# Generated by Django 2.2.4 on 2019-12-03 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_pastmovement_duration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='currentmovement',
            name='id',
        ),
        migrations.AlterField(
            model_name='currentmovement',
            name='robot',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='main.Robot'),
        ),
    ]
