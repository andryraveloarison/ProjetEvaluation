# Generated by Django 5.0.1 on 2024-01-30 19:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomClasse', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Critere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCritere', models.CharField(max_length=250)),
                ('valeur', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Lycee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomLycee', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Matiere',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomMatiere', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Prof',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomProf', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomRole', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomUser', models.CharField(max_length=250)),
                ('emailUser', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Compte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50)),
                ('idLycee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.lycee', verbose_name='relation Lycee')),
            ],
        ),
        migrations.CreateModel(
            name='ResultatEvaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCritere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.critere', verbose_name='relation Critere')),
                ('idMatiere', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.matiere', verbose_name='relation Matiere')),
                ('idProf', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.prof', verbose_name='relation Prof')),
            ],
        ),
        migrations.CreateModel(
            name='Evaluation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('idStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.status', verbose_name='relation status')),
            ],
        ),
        migrations.CreateModel(
            name='StatusUserCompte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCompte', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.compte', verbose_name='relation Compte')),
                ('idStatus', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.status', verbose_name='relation Status')),
                ('idUser', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='evaluation.user', verbose_name='relation User')),
            ],
        ),
    ]