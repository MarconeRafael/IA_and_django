# Agente AI - Back-end

Este projeto consiste no back-end de uma aplicação que processa campanhas de marketing, gerando briefs detalhados e embeddings a partir de informações fornecidas pelo usuário. A aplicação recebe dados por meio de um formulário web, armazena esses dados em um arquivo CSV e realiza o processamento necessário, como a geração de briefing e embeddings.

## Funcionalidades

- **Processamento de Campanha**: O usuário envia informações sobre uma campanha através de um formulário na web, como nome da campanha, público-alvo, objetivo, formato de conteúdo, entre outros.
- **Geração de Briefing**: O sistema processa os dados da campanha e gera um briefing detalhado, que é armazenado junto com os dados.
- **Geração de Embeddings**: Utiliza os dados coletados para gerar embeddings, que são salvos em um arquivo específico.
- **Armazenamento de Dados**: Os detalhes da campanha são armazenados em um arquivo CSV para posterior análise e utilização.
- **Redirecionamento e Notificações**: Após o processamento, o sistema redireciona o usuário para uma página de confirmação com mensagens de sucesso ou erro.

## Estrutura do Projeto

- **agente/**
  - **templates/**
    - `home.html`: Página inicial com o formulário de envio de dados.
    - `briefing.html`: Página que exibe e permite a edição do briefing gerado.
    - `concluida.html`: Página de sucesso, informando que a missão foi concluída com sucesso.
  - **utils/**
    - `briefing.py`: Função para gerar o briefing da campanha a partir dos dados fornecidos.
    - `embeddings.py`: Função para gerar embeddings a partir dos dados da campanha.
  - **views.py**: Contém as funções de visualização, como processar os dados do formulário, gerar briefing e embeddings, e redirecionar para a página de sucesso.
  - **urls.py**: Arquivo que mapeia as URLs para as views correspondentes.
  - **models.py**: (Caso necessário) Definição do modelo de dados.

## Instalação e Execução

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/Agente_AI_back_end.git
   cd Agente_AI_back_end
   
# Passos para Configuração do Ambiente

2. **Crie um ambiente virtual**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # No Windows use venv\Scripts\activate


3. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt


4. **Crie o arquivo keys.py**:
   ```bash
   cd agente
   cd utils
  crie um arquivo keys.py e adicione nele a variável chave_openai com sua chave de API da openai

  
5. **Execute o servidor**:
   ```bash
   python manage.py runserver


Abra o navegador e acesse http://127.0.0.1:8000/ para utilizar a aplicação.

## Funcionalidade do Formulário

O formulário na página inicial coleta as seguintes informações:

- Nome da campanha
- Objetivo da campanha
- Público-alvo
- Formato do conteúdo desejado
- Canal de divulgação
- Nicho de mercado
- Ações e comportamentos esperados do creator
- Comportamentos indesejados ou proibidos
- Informações adicionais
Após o envio, o sistema processa as informações, gera um briefing e embeddings, e retorna uma mensagem de sucesso ou erro.

## Contribuições

Se você deseja contribuir com este projeto, siga os passos abaixo:

- Faça o fork deste repositório.
- Crie uma branch com suas mudanças (`git checkout -b minha-branch`).
- Commit suas mudanças (`git commit -m 'Adicionando nova funcionalidade'`).
- Envie para o repositório remoto (`git push origin minha-branch`).
- Abra um pull request.


## Licença

Este projeto está licenciado sob a [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).



### Detalhes:

1. **Funcionalidades**: Descrição das principais funcionalidades do sistema, como processamento de campanhas e geração de briefing e embeddings.
2. **Estrutura do Projeto**: Explicação da estrutura do diretório, mencionando as pastas e arquivos importantes.
3. **Instalação e Execução**: Passo a passo para configurar o ambiente de desenvolvimento e rodar o servidor Django localmente.
4. **Funcionalidade do Formulário**: Detalha o que o formulário na página inicial coleta e o processo após o envio.
5. **Contribuições**: Guia para quem deseja contribuir com o projeto.
6. **Licença**: Informação sobre a licença do projeto ([Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)).



