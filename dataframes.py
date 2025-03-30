#%% Bibliotecas
import pandas as pd

#%% Importando dados - CSV (local)

# Leitura básica
csv_basico = pd.read_csv("arquivo.csv")

# Leitura com separador e decimal ajustados (ex: dados financeiros)
csv_formatado = pd.read_csv("arquivo.csv", sep=";", decimal=",")

#%% Importando dados - CSV (via link)

# Exemplo real: dados de desembolso do BNDES
bndes = pd.read_csv("http://api.bcb.gov.br/dados/serie/bcdata.sgs.7415/dados?formato=csv&dataInicial=01/01/2010&dataFinal=31/12/2020",
                    sep=";")

#%% Importando dados - Excel (local)

# Leitura básica de um arquivo Excel
excel_arquivo = pd.read_excel("arquivo.xlsx")

#%% Salvando (exportando) os dados - CSV

# Exportando sem índice, com separador padrão
csv_formatado.to_csv("csv_formatado_exportado.csv", sep=",", decimal=".", index=False)

#%% Salvando (exportando) os dados - Excel

excel_arquivo.to_excel("excel_exportado.xlsx", index=False)
