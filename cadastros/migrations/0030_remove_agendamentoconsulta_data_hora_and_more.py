# Generated by Django 4.2.5 on 2023-10-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0029_remove_agendamentoconsulta_codigo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agendamentoconsulta',
            name='data_hora',
        ),
        migrations.AddField(
            model_name='agendamentoconsulta',
            name='data',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='agendamentoconsulta',
            name='horario',
            field=models.TimeField(null=True, verbose_name='Horário'),
        ),
        migrations.AlterField(
            model_name='agendamentoconsulta',
            name='retorno',
            field=models.BooleanField(choices=[(True, 'Sim'), (False, 'Não')], default=False),
        ),
        migrations.AlterField(
            model_name='agendamentoconsulta',
            name='tipo_consulta',
            field=models.CharField(choices=[('Plano', 'Plano'), ('Particular', 'Particular')], max_length=10, verbose_name='Tipo de Consulta'),
        ),
        migrations.AlterField(
            model_name='agendamentoconsulta',
            name='valor_consulta',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor da Consulta'),
        ),
    ]
