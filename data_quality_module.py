import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class DataQualitys:
    def __init__(self, df):
        self.df = df

    def contagem_nulls(self):
        """Retorna a contagem de valores nulos por coluna."""
        return self.df.isnull().sum()

    def contagem_unicos(self):
        """Retorna a contagem de valores únicos por coluna."""
        return self.df.nunique()

    def contagem_valores_categoria(self):
        """Apresenta o value_counts de todas as colunas categóricas."""
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            print(f"Value counts for {col}:\n{self.df[col].value_counts()}\n")

    def describe_numerical(self):
        """Retorna o resumo estatístico das colunas numéricas."""
        return self.df.describe()

    def plot_categorical_distribution(self):
        """Plota gráficos de barras para colunas categóricas."""
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        for col in categorical_cols:
            self.df[col].value_counts().plot(kind='bar', title=f'Distribuição de {col}', figsize=(8, 4))
            plt.xlabel(col)
            plt.ylabel('Contagem')
            plt.show()

    def plot_numerical_distribution(self):
        """Plota histogramas para colunas numéricas."""
        numerical_cols = self.df.select_dtypes(include=[np.number]).columns
        for col in numerical_cols:
            self.df[col].plot(kind='hist', bins=30, title=f'Distribuição de {col}', figsize=(8, 4))
            plt.xlabel(col)
            plt.ylabel('Frequência')
            plt.show()


    def full_report(self):
        """Gera um relatório completo de análise."""
        print("Contagem de nulos:\n", self.contagem_nulls())
        print("\nContagem de valores únicos:\n", self.contagem_unicos())
        print("\nContagem de valores categoricos:", self.contagem_valores_categoria())
        print("\nResumo estatístico de colunas numéricas:\n", self.describe_numerical())
        print("\nDistribuição de colunas categóricas:")
        self.plot_categorical_distribution()
        print("\nDistribuição de colunas numéricas:")
        self.plot_numerical_distribution()
