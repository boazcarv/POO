
"""
Implemente a solução em um único arquivo Python. Utilize type hints em todos os atributos,
parâmetros e retornos de método. Nomeie classes, atributos e métodos de forma clara e
condizente com o domínio do problema. O atendimento a esses itens será avaliado nesta prova.
• Ao final, inclua no seu arquivo um bloco de demonstração (sob if __name__ == "__main__":) que
instancie a classe e exercite o funcionamento de todos os métodos implementados, incluindo os
casos de exceção.
• Programas que não executem apropriadamente poderam ter sua pontuação ZERADA.

Contexto:
A farmácia de uma Unidade de Pronto Atendimento (UPA) precisa controlar, de forma individual, cada
lote de medicamento em seu estoque. Cada lote possui um medicamento (nome), um código de lote,
uma data de validade, uma quantidade de unidades disponíveis e um valor unitário. A farmácia precisa:
cadastrar um lote; consultar seus dados de forma padronizada; registrar a dispensação (saída) e a
reposição (entrada) de unidades, impedindo que o estoque fique negativo e impedindo a dispensação
de um lote já vencido; comparar dois lotes para saber se representam o mesmo medicamento e mesmo
lote; e ordenar uma lista de lotes pela proximidade da validade, para priorizar o que está prestes a
vencer.
1. Modele uma única classe Python, Medicamento, que atenda a todos os requisitos descritos,
conforme o detalhamento dos itens a seguir, em que cada item vale 10 pontos.
a. Nomes de classes, atributos, métodos, parâmetros e exceções devem seguir as convenções
do Python (PEP 8) e refletir claramente o domínio do problema farmacêutico, em toda a solução
entregue (este item é avaliado de forma transversal a todos os itens da avaliação).
b. Defina a classe Medicamento com “construtor” (__init__()) tipado (parâmetros), recebendo
nome: str, lote: str, validade: date, quantidade: int e valor: float.
Os atributos quantidade e valor devem ser expostos por meio de @property e protegidos com

um setter que valide o estado: quantidade não pode ser um valor negativo e valor deve ser
estritamente maior que zero, caso contrário, lance ValueError com uma mensagem clara. A
validação deve valer tanto na criação do objeto quanto em qualquer atribuição posterior a esses
atributos.
c. Implemente um método de classe (@classmethod) chamado de_registro(), que receba
uma única string no formato "nome;lote;validade;quantidade;valor" (com a validade em formato
ISO, "AAAA-MM-DD") e retorne uma instância de Medicamento já construída a partir desses
dados. Implemente também um método estático (@staticmethod) chamado
dias_para_vencer(), que receba uma data de validade (date) e devolva, como int, a
quantidade de dias entre a data atual (date.today()) e essa validade, sem depender de
nenhuma instância da classe.
d. Implemente __str__(), retornando uma descrição legível do lote (medicamento, lote,
quantidade e validade); __repr__(), retornando uma representação voltada à depuração;
__eq__(), considerando dois objetos Medicamento iguais quando possuem o mesmo nome
e o mesmo lote; e __lt__(), comparando dois objetos pela data de validade, de forma que
uma lista de objetos Medicamento possa ser ordenada com sorted() da validade mais
próxima para a mais distante.
e. Crie as exceções QuantidadeInvalidaError e MedicamentoVencidoError (ambas
herdando de Exception). Implemente o método dispensar(quantidade: int), que
deve: lançar QuantidadeInvalidaError se a quantidade solicitada for menor ou igual a
zero, ou maior do que a quantidade disponível em estoque; lançar
MedicamentoVencidoError se a data de validade do lote já tiver passado (comparando com
date.today()); e, se nenhuma dessas condições ocorrer, reduzir a quantidade em estoque.
Implemente também repor(quantidade: int), que aumenta a quantidade em estoque,
reaproveitando a validação já existente no setter do item (a).
"""

from __future__ import annotations

from datetime import date

class QuantidadeInvalidaError(Exception):
    pass

class MedicamentoVencidoError(Exception):
    pass

class Medicamento:
    def __init__(self, nome: str, lote: str, validade: date, quantidade: int, valor: float):
        self.nome = nome
        self.lote = lote
        self.validade = validade
        self._quantidade = quantidade
        self._valor = valor

    @property
    def quantidade(self) -> int:
        return self._quantidade

    @quantidade.setter
    def quantidade(self, quantidade: int) -> None:
        if not isinstance(quantidade, int):
            raise ValueError("[Erro - Quantidade inválida] A quantidade deve ser um número inteiro.")
        if quantidade < 0:
            raise ValueError("[Erro - Quantidade negativa] A quantidade deve ser um número positivo.")
        self._quantidade = quantidade
#Até aqui esta ok
    @property
    def valor(self) -> float:
        return self._valor
#Até aqui esta ok
    @valor.setter
    def valor(self, valor: float) -> None:
        if not isinstance(valor, float):
            raise ValueError("[Erro - Valor inválido] O valor deve ser um número inteiro.")
        if valor < 0:
            raise ValueError("[Erro - Valor negativo] O valor deve ser um número positivo.")
        self._valor = valor
# parcialmente
    @classmethod
    def de_registro(cls, texto: str) -> "Medicamento":
        nome, lote, validade_texto, quantidade_texto, valor_texto = texto.split(";")
        validade = date.fromisoformat(validade_texto)
        quantidade = int(quantidade_texto)
        valor = float(valor_texto)
        return cls(nome, lote, validade, quantidade, valor)

    @staticmethod
    def dias_para_vencer(validade: date) -> int:
       hoje = date.today()
       return (validade - hoje).days

    def __str__(self) -> str:
        return f"Medicamento: {self.nome} | Lote: {self.lote} | Quantidade: {self._quantidade} | Validade: {self.validade}"

    def __repr__(self) -> str:
        return f"Depuração: Medicamento({self.nome}, {self.lote}, {self.validade}, {self.quantidade}, {self.valor})"
   # OK
    def __eq__(self, outro: object) -> bool:
        if not isinstance(outro, Medicamento):
            return NotImplemented
        return self.nome == outro.nome and self.lote == outro.lote
    
    def __lt__(self, other: Medicamento) -> bool:
        return self.validade < other.validade   

    def dispensar(self, quantidade: int) -> None:
        if quantidade <= 0 or quantidade > self.quantidade:
            raise QuantidadeInvalidaError("[Erro - Quantidade inválida] A quantidade de dispensação deve ser maior que zero e menor ou igual ao estoque atual.")
        if self.validade < date.today():
            raise MedicamentoVencidoError(f"Erro - Medicamento vencido] O lote {self.lote} está vencido.")
        self.quantidade += quantidade
   
    def repor(self, quantidade: int) -> None:
        if quantidade < 0:
            raise ValueError("[Erro - Quantidade inválida] A quantidade de reposição não pode ser negativa.")
        self.quantidade += quantidade
        
if __name__ == "__main__":
    print("Demonstração da classe Medicamento")

    m1 = Medicamento("Dipirona 500mg", "L2026A", date(2026, 12, 31), 100, 12.50)
    m2 = Medicamento.de_registro("Amoxicilina 500mg;L2026B;2026-10-15;40;18.90")

    print(f"Dados de m1: {m1}")
    print(f"Dados de m2: {m2}")
    print(f"Dias para vencer de m2: {Medicamento.dias_para_vencer(m2.validade)}")
    print(f"Representação de m1: {m1!r}")
    print(f"m1 == m2? {m1 == m2}")
    print("Dispensando 20 medicamentos de m1")
    m1.dispensar(20)
    print(f"Quantidade de m1: {m1.quantidade}")

    try:
        m2.dispensar(9999)
    except QuantidadeInvalidaError as erro:
        print(f"Erro esperado: {erro}")

    vencido = Medicamento("Soro Fisiológico", "P1B2C3G", date(2025, 1, 10), 10, 5.0)
    try:
        vencido.dispensar(1)
    except MedicamentoVencidoError as erro:
        print(f"Erro esperado: {erro}")

    outro = Medicamento("Dipirona 500mg", "V1T2V3O4", date(2026, 1, 1), 0, 1.0)
    print(f"m1 é igual a outro? {m1 == outro}")

    print("Repondo 15 unidades em m2")
    m2.repor(15)
    print(f"Quantidade de m2 após reposição: {m2.quantidade}")
# OK
    estoque: list[Medicamento] = [m1, m2, vencido, outro]
    print("Exibindo lista ordenada por validade (mais próxima primeiro):")
    for lote in sorted(estoque):
        print(f" - {lote}")

    try:
        m1.quantidade = -5
    except ValueError as erro:
        print(f"Erro esperado: {erro}")

    try:
        m1.valor = 0
    except ValueError as erro:
        print(f"Erro esperado: {erro}")

    try:
        Medicamento("Paracetamol", "L9", date(2026, 5, 1), -2, 2.5)
    except ValueError as erro:
        print(f"Erro esperado: {erro}")

    try:
        Medicamento("Ibuprofeno", "L7", date(2025, 5, 1), 3, -1.0)
    except ValueError as erro:
        print(f"Erro esperado: {erro}")