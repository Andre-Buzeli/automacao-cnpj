# Sistema de Pesquisa de Dívidas por CNPJ

Sistema para consulta de dívidas empresariais em bases de dados do FGTS, Previdência e Dívida Ativa (SIDA).

## 🚀 Deploy

Este aplicativo está configurado para deploy no Streamlit Community Cloud.

### Pré-requisitos

- Arquivos de dados em formato Parquet na pasta `data/parquet/`:
  - `estabele_consolidado.parquet`
  - `fgts_consolidado.parquet`
  - `prev_consolidado.parquet`
  - `sida_consolidado.parquet`
  - `CNAE.parquet`

### Como fazer deploy

1. Faça fork deste repositório ou clone para sua conta GitHub
2. Certifique-se de que os arquivos de dados estão na pasta `data/parquet/`
3. Acesse [share.streamlit.io](https://share.streamlit.io)
4. Conecte sua conta GitHub
5. Selecione este repositório
6. Configure:
   - **Main file path**: `streamlit_app.py`
   - **Python version**: 3.9+
7. Clique em "Deploy"

## 🔧 Funcionalidades

- **Pesquisa por valor**: Filtragem por faixa de valores de dívida
- **Filtro por estado**: Seleção por UF
- **Classificação CNAE**: Filtros por seção e divisão de atividade econômica
- **Tipos de dívida**: FGTS, Previdência, Dívida Ativa ou todas
- **Resultados em tempo real**: Processamento e exibição progressiva
- **Download seletivo**: Baixar registros selecionados ou todos os resultados
- **Formatação brasileira**: Valores monetários e dados formatados para o padrão brasileiro

## 📊 Dados

O sistema utiliza dados consolidados de diferentes fontes governamentais:

- **Estabelecimentos**: Base de dados do CNPJ da Receita Federal
- **FGTS**: Débitos do Fundo de Garantia do Tempo de Serviço
- **Previdência**: Débitos previdenciários
- **SIDA**: Sistema de Dívida Ativa da União
- **CNAE**: Classificação Nacional de Atividades Econômicas

## 🛠️ Tecnologias

- **Streamlit**: Interface web
- **DuckDB**: Banco de dados analítico para consultas rápidas
- **Pandas**: Manipulação de dados
- **Python 3.9+**: Linguagem de programação

## 📝 Licença

Este projeto é destinado para fins educacionais e de pesquisa. Os dados utilizados são de domínio público disponibilizados pelos órgãos governamentais competentes.