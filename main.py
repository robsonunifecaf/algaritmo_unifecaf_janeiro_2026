from imovel import Imovel
from orcamento import Orcamento

tipo = input("Tipo de imóvel (apartamento/casa/estudio): ").lower()

quartos = 1
garagem = False
vagas_estudio = 0
possui_criancas = False

if tipo in ["apartamento", "casa"]:
    quartos = int(input("Quantidade de quartos (1 ou 2): "))
    garagem = input("Possui garagem? (s/n): ").lower() == "s"
    possui_criancas = input("Possui crianças? (s/n): ").lower() == "s"

elif tipo == "estudio":
    vagas_estudio = int(input("Quantidade de vagas: "))

imovel = Imovel(tipo, quartos, garagem, vagas_estudio, possui_criancas)
valor_aluguel = imovel.calcular_aluguel()

orcamento = Orcamento(valor_aluguel)

print(f"\nValor do aluguel mensal: R$ {valor_aluguel:.2f}")
print("Valor do contrato: R$ 2000,00 (até 5x de R$ 400,00)")

gerar = input("Deseja gerar o arquivo CSV? (s/n): ").lower()

if gerar == "s":
    orcamento.gerar_csv()
    print("Arquivo parcelas.csv gerado com sucesso.")
