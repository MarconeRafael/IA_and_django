import openai
import pandas as pd
import os
from .keys import chave_openai

# Configuração da chave da API
openai.api_key = chave_openai

# Função para truncar textos longos
def truncar_texto(texto, max_tokens=8192):
    if texto is None:
        return ""
    return texto[:max_tokens] if len(texto) > max_tokens else texto

# Função para sanitizar texto
def sanitizar_texto(texto):
    if pd.isna(texto):
        return "Não informado"
    return str(texto).replace('**', '').replace('""', '"').strip()

# Função para gerar embeddings
def gerar_embeddings(caminho_csv):
    try:
        # Verifica se o arquivo existe
        if not os.path.exists(caminho_csv):
            print(f"Arquivo {caminho_csv} não encontrado.")
            return

        # Carrega o arquivo CSV
        df = pd.read_csv(caminho_csv)

        # Verifica se o DataFrame está vazio
        if df.empty:
            print("O arquivo CSV está vazio.")
            return

        embeddings = []

        for _, row in df.iterrows():
            # Concatena os campos necessários
            texto = "\n".join([
                f"Nome da Campanha: {sanitizar_texto(row.get('Nome da Campanha'))}",
                f"Objetivo: {sanitizar_texto(row.get('Objetivo'))}",
                f"Público-Alvo: {sanitizar_texto(row.get('Público-Alvo'))}",
                f"Formato do Conteúdo Desejado: {sanitizar_texto(row.get('Formato do Conteúdo Desejado'))}",
                f"Canal de Divulgação: {sanitizar_texto(row.get('Canal de Divulgação'))}",
                f"Briefing: {truncar_texto(sanitizar_texto(row.get('Briefing')), max_tokens=3000)}",
                f"Roteiro: {truncar_texto(sanitizar_texto(row.get('Roteiro')), max_tokens=3000)}",
            ])

            try:
                # Gera o embedding
                response = openai.Embedding.create(
                    input=texto,
                    model="text-embedding-ada-002"
                )
                embedding = response['data'][0]['embedding']
                embeddings.append(embedding)
                print("Embedding gerado com sucesso.")
            except Exception as e:
                print(f"Erro ao gerar embedding para a linha: {e}")
                # Adiciona valores nulos para dimensões do embedding em caso de erro
                embeddings.append([None] * 1536)

        # Converte para DataFrame
        embeddings_df = pd.DataFrame(
            embeddings, 
            columns=[f"dim_{i}" for i in range(1536)]
        )

        # Salva os embeddings em um novo arquivo
        output_path = "csvs/embeddings.csv"
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        embeddings_df.to_csv(output_path, index=False)
        print(f"Embeddings gerados e salvos com sucesso em {output_path}.")
    except Exception as e:
        print(f"Erro ao processar: {e}")

# Chamada da função
gerar_embeddings("csvs/campanha_detalhes.csv")
