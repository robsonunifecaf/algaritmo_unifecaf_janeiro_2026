import csv

class Orcamento:
    def __init__(self, valor_aluguel):
        self.valor_aluguel = valor_aluguel
        self.valor_contrato = 2000

    def gerar_csv(self):
        with open("parcelas.csv", mode="w", newline="", encoding="utf-8") as arquivo:
            writer = csv.writer(arquivo)
            writer.writerow(["Parcela", "Valor"])

            for i in range(1, 13):
                writer.writerow([i, f"{self.valor_aluguel:.2f}"])
