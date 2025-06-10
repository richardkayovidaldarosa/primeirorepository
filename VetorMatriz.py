#Lista de alunos (vetor)
alunos = ["Alice", "Bruno","Carla"] 

# Dias da semana (colunas da matriz)
dias = ["Seg", "Ter" "Qua", "Qui"]

# Criar uma matriz vazia de reservas (valores padrão: 'Ausente')
reservas = [["Ausente" for_in dias] for_in alunos]

# Preencher a matriz com dados inseridos pelo usuário
print (Preencha com 'S' para presença e 'X' para ausência:")

for i, aluno in enumerate(alunos):
print(f"\nAluno: {aluno}")
for j, dia in enumerate(dias):
    entrada = input (f"  {dia}: ")
    if entrada.upper() == 'S':
        reservas [i][j] = "Presente

# Exibir a tabela final
print(\nTabela de Reservas:")
print(f"{'aluno'}:<10} {'  '.join([f'{d:<10}' for d in dias])}")
for i, aluno in enumerate(alunos):
    print(f"aluno:{aluno<10} {}")