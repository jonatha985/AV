# Generated by Django 4.2.5 on 2023-11-10 04:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0034_agendamento_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atendimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(null=True)),
                ('anamnese_paciente', models.TextField(verbose_name='Anamnese do paciente')),
                ('diagnostico', models.TextField(verbose_name='Diagnóstico')),
                ('receituario', models.TextField(verbose_name='Receituário/Recomendações')),
                ('procedimento', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='cadastros.agendamento')),
            ],
        ),
        migrations.RenameField(
            model_name='procedimento',
            old_name='nome',
            new_name='nome_procedimento',
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='especialidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.especialidade'),
        ),
        migrations.DeleteModel(
            name='Nota',
        ),
    ]
