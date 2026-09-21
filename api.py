# Aluno(a): Pablo Boaz Carvalho Gomes
# Professor: Higor Morais
# Turma: TSI 2026.2

# Lista de Exercícios (POO) - Fundamentos

# Questão 6 - Classe Aluno

class Aluno:
    # Inicializa o aluno com nome, matrícula e uma lista vazia de notas.
    def __init__(self, nome: str, matricula: str):
        self.nome = nome
        self.matricula = matricula
        self.notas = []

    # Adiciona uma nova nota à lista de notas do aluno.
    def lancar_nota(self, valor: float):
        self.notas.append(valor)

    # Calcula a média aritmética das notas lançadas.
    # Caso não existam notas, retorna 0.0 para evitar divisão por zero.
    def media(self) -> float:
        if not self.notas:
            return 0.0
        return sum(self.notas) / len(self.notas)

    # Verifica se a média do aluno é igual ou superior a 6.0.
    def aprovado(self) -> bool:
        return self.media() >= 6.0

    # Define como o aluno será apresentado quando for convertido para texto.
    def __str__(self) -> str:
        return f"{self.nome} ({self.matricula}) — média {self.media():.1f}"


# Questão 7 - Criar 3 alunos, lançar notas e imprimir apenas os aprovados
# Nesta etapa, são criados três objetos da classe Aluno.

aluno1 = Aluno("Ana", "20261234")
# Lança duas notas para Ana.
aluno1.lancar_nota(7.0)
aluno1.lancar_nota(8.0)

aluno2 = Aluno("Bruno", "20261235")
# Lança duas notas para Bruno.
aluno2.lancar_nota(4.0)
aluno2.lancar_nota(5.0)

aluno3 = Aluno("Carla", "20261236")
# Lança duas notas para Carla.
aluno3.lancar_nota(6.0)
aluno3.lancar_nota(10.0)

# Percorre todos os alunos e exibe somente aqueles que foram aprovados.
print("Alunos aprovados:")
for aluno in [aluno1, aluno2, aluno3]:
    if aluno.aprovado():
        print(aluno)


# Questão 8 - Classe Retangulo

class Retangulo:
    # Guarda as medidas da base e da altura do retângulo.
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    # Calcula a área multiplicando a base pela altura.
    def area(self) -> float:
        return self.base * self.altura

    # Calcula o perímetro somando todos os lados do retângulo.
    def perimetro(self) -> float:
        return 2 * (self.base + self.altura)

    # Compara dois retângulos pela base e pela altura.
    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Retangulo):
            return NotImplemented
        return self.base == outro.base and self.altura == outro.altura


# Cria três retângulos para testar os métodos da classe.
r1 = Retangulo(4, 6)
r2 = Retangulo(4, 6)
r3 = Retangulo(3, 8)

# Exibe a área, o perímetro e os resultados das comparações.
print(r1.area())       # 24
print(r1.perimetro())  # 20
print(r1 == r2)        # True
print(r1 == r3)        # False


# Questão 9 - Classe Data

class Data:
    # Inicializa uma data com dia, mês e ano.
    def __init__(self, dia: int, mes: int, ano: int):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    # Cria uma data a partir de um texto no formato dia/mês/ano.
    @classmethod
    def de_texto(cls, texto: str) -> "Data":
        dia, mes, ano = map(int, texto.split("/"))
        return cls(dia, mes, ano)

    # Verifica se o ano é bissexto pelas regras do calendário gregoriano.
    @staticmethod
    def bissexto(ano: int) -> bool:
        return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

    # Formata a data com dois dígitos para dia e mês e quatro para o ano.
    def __str__(self) -> str:
        return f"{self.dia:02d}/{self.mes:02d}/{self.ano:04d}"


# Cria uma data diretamente e outra usando o método de conversão de texto.
d1 = Data(9, 8, 2026)
d2 = Data.de_texto("25/12/2026")

# Exibe as datas e testa quais anos são bissextos.
print(d1)                   # 09/08/2026
print(d2)                   # 25/12/2026
print(Data.bissexto(2024))  # True
print(Data.bissexto(2026))  # False
