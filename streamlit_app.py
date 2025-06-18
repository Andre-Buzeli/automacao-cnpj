import duckdb
import streamlit as st
import pandas as pd
import time
import os

# Configuração da página
st.set_page_config(
    page_title="Sistema de Pesquisa de Dívidas - CNPJ",
    page_icon="🔍",
    layout="wide"
)

st.title("🔍 Sistema de Pesquisa de Dívidas por CNPJ")

# Verificar se os arquivos de dados existem
data_dir = "data/parquet"
required_files = [
    "estabele_consolidado.parquet",
    "fgts_consolidado.parquet", 
    "prev_consolidado.parquet",
    "sida_consolidado.parquet",
    "CNAE.parquet"
]

missing_files = []
for file in required_files:
    if not os.path.exists(os.path.join(data_dir, file)):
        missing_files.append(file)

if missing_files:
    st.error(f"""
    ❌ **Arquivos de dados não encontrados:**
    
    Os seguintes arquivos são necessários na pasta `{data_dir}`:
    {chr(10).join(f'• {file}' for file in missing_files)}
    
    Por favor, certifique-se de que os arquivos Parquet estão disponíveis para o funcionamento do sistema.
    """)
    st.stop()

# Interface simplificada quando dados não estão disponíveis
st.info("""
🔧 **Sistema em Configuração**

Este é um sistema de pesquisa de dívidas empresariais que consulta dados do:
- FGTS (Fundo de Garantia do Tempo de Serviço) 
- Previdência Social
- Dívida Ativa (SIDA)

Os arquivos de dados precisam ser adicionados na pasta `data/parquet/` para o sistema funcionar.

**Funcionalidades disponíveis:**
- Pesquisa por faixa de valores
- Filtro por estado (UF)
- Classificação por CNAE
- Download de resultados
- Interface responsiva
""")

st.markdown("---")

# Demo da interface (sem dados)
st.subheader("📋 Interface de Pesquisa")

col1, col2, col3 = st.columns([2.5, 2, 2.5])

with col1:
    st.subheader("💰 Faixa de Valor da Dívida")
    valor_min = st.number_input("Valor Mínimo (R$)", min_value=0, value=0, step=100, format="%d", disabled=True)
    valor_max = st.number_input("Valor Máximo (R$)", min_value=0, value=1000000, step=1000, format="%d", disabled=True)

with col2:
    st.subheader("📍 Estado (UF)")
    uf_opcoes = ['Todas', 'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO']
    uf_selecionada = st.selectbox("Selecione o Estado", uf_opcoes, disabled=True)
    
    st.subheader("💼 Tipo de Dívida")
    tipo_pesquisa = st.radio(
        "Selecione:",
        ["FGTS", "Previdência", "Dívida Ativa (SIDA)", "Todas"],
        index=3,
        disabled=True
    )

with col3:
    st.subheader("🏭 Atividade Econômica (CNAE)")
    
    secoes_demo = [
        "Todas",
        "A - AGRICULTURA, PECUÁRIA...",
        "B - INDÚSTRIAS EXTRATIVAS", 
        "C - INDÚSTRIAS DE TRANSFORMAÇÃO",
        "F - CONSTRUÇÃO",
        "G - COMÉRCIO; REPARAÇÃO DE VEÍCULOS"
    ]
    
    secao_selecionada = st.selectbox("Seção CNAE", secoes_demo, disabled=True)
    divisao_selecionada = st.selectbox("Divisão CNAE", ["Todas"], disabled=True)
    
    st.info("""
    **💡 Funcionalidades:** 
    - FGTS: Débitos do Fundo de Garantia
    - Previdência: Débitos previdenciários  
    - Dívida Ativa: Débitos SIDA
    - Resultados em tempo real
    - Download seletivo
    """)

st.markdown("---")

# Botão de pesquisa (desabilitado)
col_btn1, col_btn2, col_btn3 = st.columns([2, 2, 2])
with col_btn2:
    st.button("🔍 Pesquisar Dívidas", type="primary", use_container_width=True, disabled=True)

st.info("🔧 Para ativar o sistema, adicione os arquivos de dados na pasta `data/parquet/`")

# Exemplo de resultados
st.markdown("---")
st.subheader("📊 Exemplo de Resultados")

# Dados de exemplo para demonstração
exemplo_dados = {
    'CNPJ': ['12.345.678/0001-90', '98.765.432/0001-10', '11.222.333/0001-44'],
    'Razão Social': ['EMPRESA EXEMPLO LTDA', 'COMERCIO DEMO LTDA', 'INDUSTRIA TESTE SA'],
    'Tipo Dívida': ['FGTS', 'Previdência', 'Dívida Ativa'],
    'Valor': ['R$ 15.750,00', 'R$ 8.320,50', 'R$ 125.680,75'],
    'Situação': ['Ativa', 'Ativa', 'Ativa']
}

df_exemplo = pd.DataFrame(exemplo_dados)
df_exemplo.insert(0, '✓', [False, False, False])

st.data_editor(
    df_exemplo,
    column_config={
        "✓": st.column_config.CheckboxColumn(
            "Selecionar",
            help="Exemplo de seleção",
            default=False,
        )
    },
    disabled=True,
    hide_index=True,
    use_container_width=True
)

st.success("📋 Exemplo: Interface mostrando como os resultados seriam apresentados com dados reais")