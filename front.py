#A média dos alunos
class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if 0 <= nota <= 10:
            self.notas.append(nota)
        else:
            print(f"Nota inválida: {nota}. Deve estar entre 0 e 10.")

    def calcular_media(self):
        if self.notas:
            return sum(self.notas) / len(self.notas)
        else:
            return 0.0


class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def exibir_medias(self):
        print("Médias dos Alunos:")
        for aluno in self.alunos:
            media = aluno.calcular_media()
            print(f"Aluno: {aluno.nome}, Média: {media:.2f}")


# Função principal
def main():
    turma = Turma()

    for i in range(1, 6):
        nome = input(f"Digite o nome do aluno {i}: ")
        aluno = Aluno(nome)
        print(f"Adicionando notas para {nome} (digite -1 para encerrar):")
        
        while True:
            try:
                nota = float(input("Digite a nota: "))
                if nota == -1:
                    break
                aluno.adicionar_nota(nota)
            except ValueError:
                print("Por favor, insira um número válido.")
        
        turma.adicionar_aluno(aluno)

    turma.exibir_medias()


if __name__ == "__main__":
    main()
