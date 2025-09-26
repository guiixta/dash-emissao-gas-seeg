# Dashboard de Emissões de GEE no Brasil 🇧🇷

## 📄 Sobre o Projeto

Este é um dashboard interativo para a visualização de dados sobre a emissão de gases de efeito estufa (GEE) no Brasil. A aplicação foi desenvolvida em Python utilizando o framework Dash e a biblioteca Plotly para a criação de gráficos dinâmicos e informativos.

O objetivo principal é permitir que os usuários explorem os dados históricos de emissões, aplicando diversos filtros para analisar o impacto de diferentes setores, atividades econômicas e tipos de gases ao longo do tempo.

## ✨ Funcionalidades

- **Visualização Interativa**: Gráficos de barras, linhas e pizza que se atualizam dinamicamente com base nos filtros selecionados.
- **Filtros Detalhados**: Filtre os dados por:
  - Setor (ex: Agropecuária, Energia, Indústria)
  - Processo Emissor
  - Tipo de Gás
  - Atividade Econômica
  - E muito mais...
- **Análise Temporal**: Selecione um intervalo de anos específico para analisar o crescimento ou a redução das emissões.
- **Cards Informativos**: Métricas chave como emissão total, ano com maior/menor emissão e totais por período são exibidas de forma clara.
- **Design Responsivo**: A interface se adapta a diferentes tamanhos de tela.

## 📊 Fonte dos Dados

Os dados utilizados neste projeto são provenientes do **Sistema de Estimativas de Emissões e Remoções de Gases de Efeito Estufa (SEEG)** e foram obtidos através da plataforma **Base dos Dados**.

- **Conjunto de dados**: `br_seeg_emissoes`
- **Organização**: SEEG

## 🚀 Tecnologias Utilizadas

- **Python**: Linguagem principal do projeto.
- **Dash**: Framework para a construção da interface web.
- **Plotly**: Biblioteca para a criação dos gráficos interativos.
- **Pandas**: Biblioteca para manipulação e análise dos dados.
- **Tailwind CSS**: Framework CSS para estilização da interface.

## ⚙️ Como Executar o Projeto Localmente

Siga os passos abaixo para rodar o dashboard em sua máquina.

### Pré-requisitos

- **Python 3.8+**
- **Pip** (gerenciador de pacotes do Python)

### Passos

1. **Clone o repositório**:
   ```bash
   git https://github.com/guiixta/dash-emissao-gas-seeg
   cd dash-emissao-gas-seeg
   ```

2. **Crie e ative um ambiente virtual** (recomendado):
   ```bash
   # Para Windows
   python -m venv venv
   .\venv\Scripts\activate

   # Para macOS/Linux
   python -m venv venv
   source venv/bin/activate
   ```

3. **Instale as dependências**:
    Um arquivo chamado `requirements.txt` na raiz do projeto com o seguinte conteúdo:
   ```
   pandas
   plotly
   dash
   ```
   Em seguida, instale as bibliotecas com o comando:
   ```bash
   pip install -r requirements.txt
   ```

4. **Estrutura de arquivos**:
   Certifique-se de que a estrutura de pastas do seu projeto está assim:
   ```
   .
   ├── app.py
   ├── requirements.txt
   ├── assets/
   │   ├── baseDosDados.png
   │   └── seegLogo.png
   └── db/
       └── br_seegEmissoes.csv
   ```
   - O arquivo `br_seegEmissoes.csv` deve estar dentro de uma pasta chamada `db`.
   - As imagens do rodapé (`baseDosDados.png` e `seegLogo.png`) devem estar dentro da pasta `assets`.

5. **Execute a aplicação**:
   ```bash
   python app.py
   ```

6. **Acesse o dashboard**:
   Abra seu navegador e acesse `http://127.0.0.1:8050/`.

## 👨‍💻 Autor

Feito por **Guiixta**
