# Generated by Django 2.2.4 on 2019-12-02 23:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20191202_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('Right', 'Derecha'), ('Left', 'Izquierda'), ('Front', 'Avanzar'), ('Back', 'Retroceder')], default='Front', max_length=30)),
                ('robot', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.Robot')),
            ],
        ),
        migrations.CreateModel(
            name='PastMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direction', models.CharField(choices=[('Right', 'Derecha'), ('Left', 'Izquierda'), ('Front', 'Avanzar'), ('Back', 'Retroceder')], max_length=30)),
                ('runtime_date', models.DateTimeField()),
                ('robot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Robot')),
            ],
        ),
        migrations.RemoveField(
            model_name='past_movement',
            name='robot',
        ),
        migrations.DeleteModel(
            name='Current_movement',
        ),
        migrations.DeleteModel(
            name='Past_movement',
        ),
    ]
