# Generated by Django 4.2.5 on 2023-10-16 05:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0012_agendamentoconsulta_procedimentoagendado_tabelapreco_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='especialidade',
            name='valor_consulta',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.DeleteModel(
            name='TabelaPreco',
        ),
    ]
