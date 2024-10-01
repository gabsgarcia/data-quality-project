import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataQualitys:
    def __init__(self, df, max_columns=15):
        assert isinstance(df, pd.DataFrame), "O objeto fornecido não é um DataFrame."
        assert not df.empty, "O DataFrame está vazio."

        self.df = df
        self.max_columns = max_columns # Limitar número de colunas a serem plotadas

    def contagem_nulls(self):
        # Retorna a contagem de valores nulos por coluna.
        return self.df.isnull().sum()

    def contagem_unicos(self):
        #Retorna a contagem de valores únicos por coluna.
        return self.df.nunique()

    def contagem_valores_categoria(self):
        # Apresenta o value_counts de todas as colunas categóricas.
        df_cat = self.df.select_dtypes(exclude = np.number)
        if len(df_cat) == 0:
            print("Nenhuma coluna categórica encontrada.")
            return
        for coluna in df_cat.columns[:self.max_columns]:
            print(f"\nCOLUNA = {coluna}")
            print(df_cat[coluna].value_counts(dropna = False).reset_index())
            print(" ")


    def describe_numeros(self):
        # Retorna o resumo estatístico das colunas numéricas.
        df_num = self.df.select_dtypes(include = np.number)
        if len(df_num) == 0:
            print("Nenhuma coluna numérica encontrada.")
            return
        return df_num.describe()

    def plot_categoria(self):
        # Plota as colunas categóricas limitando o número de colunas e entradas.
        df_cat = self.df.select_dtypes(exclude = np.number)
        if len(df_cat) == 0:
            print("Nenhuma coluna categórica encontrada.")
            return
        for col in df_cat[:self.max_columns]:  # Limita ao número máximo de colunas
            value_counts = self.df[col].value_counts().head(15)  # Mostra apenas as 15 categorias mais frequentes
            value_counts.plot(kind='bar', title=f'Distribuição de {col} (Top 15)', figsize=(8, 4))
            plt.xlabel(col)
            plt.ylabel('Contagem')
            plt.show()

    def plot_numeros(self):
        # Plota as colunas numéricas limitando o número de colunas e entradas.
        df_num = self.df.select_dtypes(include = np.number)
        if len(df_num) == 0:
            print("Nenhuma coluna numérica encontrada.")
            return
        for col in df_num[:self.max_columns]:  # Limita ao número máximo de colunas
            self.df[col].plot(kind='hist', bins=30, title=f'Distribuição de {col}', figsize=(8, 4))
            plt.xlabel(col)
            plt.ylabel('Frequência')
            plt.show()


    def full_report(self):
        # Gera um relatório completo de análise.
        print("Contagem de nulos:\n", self.contagem_nulls())
        print("\nContagem de valores únicos:\n", self.contagem_unicos())
        print("\nContagem de valores categoricos:\n", self.contagem_valores_categoria())
        print("\nResumo estatístico de colunas numéricas:\n", self.describe_numeros())
        print("\nDistribuição de colunas categóricas:")
        self.plot_categoria()
        print("\nDistribuição de colunas numéricas:")
        self.plot_numeros()
