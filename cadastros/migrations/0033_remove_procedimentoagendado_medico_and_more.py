# Generated by Django 4.2.5 on 2023-11-09 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0032_alter_agendamentoconsulta_consulta_realizada'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedimentoagendado',
            name='medico',
        ),
        migrations.RemoveField(
            model_name='procedimentoagendado',
            name='paciente',
        ),
        migrations.RemoveField(
            model_name='procedimentoagendado',
            name='procedimento',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='codigo',
        ),
        migrations.AddField(
            model_name='procedimento',
            name='nome',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='agendamentoconsulta',
            name='tipo_consulta',
            field=models.CharField(choices=[('Plano', 'Plano'), ('Particular', 'Particular')], default='Particular', max_length=10, verbose_name='Tipo de Consulta'),
        ),
        migrations.DeleteModel(
            name='HorarioAgenda',
        ),
        migrations.DeleteModel(
            name='ProcedimentoAgendado',
        ),
    ]