# Generated by Django 5.0.3 on 2024-06-03 08:36

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Enseignant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Salle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Materiel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('budget', models.CharField(choices=[('COURANT', 'Budget courant'), ('PROJETS', 'Budget projets'), ('EXCEPTIONNEL', 'Budget financements exceptionnels')], max_length=20)),
                ('accessoires', models.TextField()),
                ('possesseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='possesseur_materiel', to='materiel.enseignant')),
                ('responsable', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responsable_materiel', to='materiel.enseignant')),
                ('localisation', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiel.salle')),
            ],
        ),
        migrations.CreateModel(
            name='Historique',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('occasion', models.CharField(max_length=100)),
                ('etat_accessoires', models.TextField()),
                ('ancien_possesseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ancien_possesseur', to='materiel.enseignant')),
                ('nouveau_possesseur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nouveau_possesseur', to='materiel.enseignant')),
                ('materiel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiel.materiel')),
                ('lieu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiel.salle')),
            ],
        ),
    ]
