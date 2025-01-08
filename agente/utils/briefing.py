import openai
import pandas as pd
import os

# Configure a chave da API da OpenAI
from .keys import chave_openai
openai.api_key = chave_openai

def criar_prompt(campanha):
    return f"""
    Você é um especialista em marketing digital. Crie um briefing detalhado para um creator
    baseado nos seguintes dados de campanha:
    
    Nome da Campanha: {campanha.get('Nome da Campanha', 'Não informado')}
    Objetivo: {campanha.get('Objetivo', 'Não informado')}
    Público-Alvo: {campanha.get('Público-Alvo', 'Não informado')}
    Formato do Conteúdo Desejado: {campanha.get('Formato do Conteúdo Desejado', 'Não informado')}
    Canal de Divulgação: {campanha.get('Canal de Divulgação', 'Não informado')}
    Ações e Comportamentos Esperados do Creator: {campanha.get('Ações e Comportamentos Esperados do Creator', 'Não informado')}
    Comportamentos Indesejados ou Proibidos: {campanha.get('Comportamentos Indesejados ou Proibidos', 'Não informado')}
    
    Inclua as seguintes informações no briefing:
    - Propósito da campanha
    - Público-alvo
    - Mensagens principais
    - Tom de voz
    - Diretrizes visuais e quaisquer detalhes relevantes.
    """

def gerar_briefing_campanha(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return f"Arquivo não encontrado: {caminho_arquivo}"
    
    try:
        campanha_df = pd.read_csv(caminho_arquivo)
        briefings = []

        for _, campanha in campanha_df.iterrows():
            prompt = criar_prompt(campanha)
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um assistente de marketing digital."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            briefing = response['choices'][0]['message']['content'].strip()
            briefings.append(briefing)

        campanha_df['Briefing'] = briefings
        campanha_df.to_csv(caminho_arquivo, index=False, encoding='utf-8')
        return caminho_arquivo

    except openai.error.OpenAIError as e:
        return f"Erro na API OpenAI: {e}"
    except Exception as e:
        return f"Erro ao gerar briefing: {e}"

