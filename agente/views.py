from django.shortcuts import render, redirect
import os
import pandas as pd
from .utils.briefing import gerar_briefing_campanha
from .utils.embeddings import gerar_embeddings

def processar_briefing(campaign_df, caminho_arquivo):
    print("Gerando briefing da campanha...")
    try:
        briefing = gerar_briefing_campanha(caminho_arquivo)
        campaign_df['Briefing'] = briefing
        print("Briefing gerado com sucesso.")
    except Exception as e:
        print(f"Erro ao gerar briefing: {e}")
        return False, f"Erro ao gerar briefing: {e}"
    return True, "Briefing gerado com sucesso."


def executar_processo(request):
    if request.method == 'POST':
        print("Coletando dados do formulário...")

        # Coleta os dados do formulário
        data = {
            "Nome da Campanha": request.POST.get('nome_campanha'),
            "Objetivo": request.POST.get('objetivo'),
            "Público-Alvo": request.POST.get('publico_alvo'),
            "Formato do Conteúdo Desejado": request.POST.get('formato_conteudo'),
            "Canal de Divulgação": request.POST.get('canal_divulgacao'),
            "Nicho de Mercado": request.POST.get('nicho_mercado'),
            "Ações e Comportamentos Esperados do Creator": request.POST.get('acoes_esperadas'),
            "Comportamentos Indesejados ou Proibidos": request.POST.get('comportamentos_indesejados'),
            "Informações Adicionais": request.POST.get('informacoes_adicionais'),
        }

        # Salvar os detalhes da campanha em um CSV
        campaign_df = pd.DataFrame([data])
        file_name = "csvs/campanha_detalhes.csv"
        file_path = os.path.join(os.getcwd(), file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        campaign_df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Detalhes da campanha salvos em: {file_path}")

        # Processar o briefing
        sucesso, mensagem_briefing = processar_briefing(campaign_df, file_path)
        if not sucesso:
            return render(request, 'home.html', {"erro": mensagem_briefing})

        # Gerar embeddings
        print("Gerando embeddings...")
        try:
            caminho_embeddings = gerar_embeddings(file_path)
            print(f"Embeddings gerados e salvos em: {caminho_embeddings}")
            mensagem_embeddings = f"Embeddings gerados e salvos em: {caminho_embeddings}"
        except Exception as e:
            mensagem_embeddings = f"Erro ao gerar embeddings: {e}"
            print(mensagem_embeddings)
            return render(request, 'home.html', {"erro": mensagem_embeddings})

        # Redireciona para a página de briefing
        return redirect('briefing')  # Redireciona para a página de briefing após o processamento

    # Renderiza a página inicial para GET
    return render(request, 'home.html')

def briefing(request):
    # Carregar o arquivo CSV
    file_path = os.path.join(os.getcwd(), 'csvs/campanha_detalhes.csv')

    try:
        campaign_df = pd.read_csv(file_path, encoding='utf-8')
        briefing_text = campaign_df['Briefing'].iloc[0]  # Pega o briefing da primeira linha
    except Exception as e:
        return render(request, 'error.html', {"erro": str(e)})

    if request.method == 'POST':
        # Atualizar o briefing com os novos dados enviados
        new_briefing = request.POST.get('briefing')
        campaign_df['Briefing'] = new_briefing
        campaign_df.to_csv(file_path, index=False, encoding='utf-8')

        return redirect('concluida')  # Redireciona para a página de missão concluída
    
    return render(request, 'briefing.html', {"briefing_text": briefing_text})


def missao_concluida(request):
    return render(request, 'concluida.html')  # Página simples com a mensagem de missão concluída
