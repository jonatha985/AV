# Generated by Django 4.2.5 on 2023-10-05 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0004_alter_medico_endereco'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agendamento_Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=15)),
                ('agendamento', models.DateTimeField()),
                ('tipo_consulta', models.CharField(choices=[('Plano', 'Plano'), ('Particular', 'Particular')], max_length=10)),
                ('retorno', models.BooleanField(default=False)),
            ],
        ),
        migrations.RenameField(
            model_name='prontuario',
            old_name='pertence',
            new_name='paciente',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='cpf',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='data',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='hora',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='medico',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='nome_paciente',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='prontuario',
        ),
        migrations.RemoveField(
            model_name='procedimento',
            name='tipo_procedimento',
        ),
        migrations.AddField(
            model_name='procedimento',
            name='descricao',
            field=models.CharField(max_length=50, null=True, verbose_name='Descricão'),
        ),
        migrations.AddField(
            model_name='procedimento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=8, null=True),
        ),
        migrations.AlterField(
            model_name='cargo',
            name='nome_cargo',
            field=models.CharField(max_length=50, unique=True, verbose_name='Nome do cargo'),
        ),
        migrations.AlterField(
            model_name='especialidade',
            name='especialidade',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='rg',
            field=models.CharField(max_length=13, unique=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='telefone',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='email',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='rg',
            field=models.CharField(max_length=13, unique=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='telefone',
            field=models.CharField(max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(max_length=14, unique=True, verbose_name='CPF'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='endereco',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='cadastros.endereco'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rg',
            field=models.CharField(max_length=13, unique=True, verbose_name='RG'),
        ),
        migrations.AlterField(
            model_name='procedimento',
            name='observacao',
            field=models.TextField(null=True, verbose_name='Observações Gerais Sobre o Procedimento'),
        ),
        migrations.DeleteModel(
            name='Anotacao',
        ),
        migrations.DeleteModel(
            name='Tipo_procedimento',
        ),
        migrations.AddField(
            model_name='agendamento_consulta',
            name='medico',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.medico'),
        ),
        migrations.AddField(
            model_name='agendamento_consulta',
            name='paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cadastros.paciente'),
        ),
    ]
