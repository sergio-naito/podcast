import streamlit as st
import pandas as pd
import math

# Carregar o arquivo CSV
@st.cache_data
def carregar_dados():
    return pd.read_csv('podcast#1#365.csv', encoding='latin1', delimiter=';')

df = carregar_dados()

# Converter a coluna Tempo_audio para horas:minutos:segundos
def converter_tempo(tempo):
    horas, minutos, segundos = map(int, tempo.split(':'))
    return horas * 3600 + minutos * 60 + segundos

df['Tempo_audio'] = df['Tempo_audio'].apply(converter_tempo)

# Função para listar todos os podcasts
def listar_todos_podcasts():
    st.title('Lista de Todos os Podcasts')
    st.write(df)
    total_segundos = df['Tempo_audio'].sum()
    minutos, segundos = divmod(total_segundos, 60)
    segundos_truncados = math.floor(segundos * 100) / 100  # Truncar para 2 casas decimais
    st.write(f'Tempo total: {minutos} minutos e {segundos_truncados} segundos')

# Menu lateral esquerdo
st.sidebar.title('Menu')

# Opções do menu
opcao = st.sidebar.radio('Selecione uma opção:', ['Listar todos os podcasts', 'Pesquisa', 'Ajuda'])

# Página de pesquisa
if opcao == 'Pesquisa':
    st.title('Pesquisa de Podcast: Telegram e Spotify')
    


    # Opção de pesquisa
    tipo_pesquisa = st.selectbox('Selecione o tipo de pesquisa:', ['Número do Podcast', 'Mês', 'Palavra-chave no Tema'])

    # Pesquisa por número do podcast
    if tipo_pesquisa == 'Número do Podcast':
        numero_podcast = st.number_input('Digite o número do podcast:', min_value=1, max_value=365, step=1)
        if st.button('Pesquisar'):
            resultado = df[df['PodCast'] == numero_podcast]
            total_segundos = resultado['Tempo_audio'].sum()
            minutos, segundos = divmod(total_segundos, 60)
            segundos_truncados = math.floor(segundos * 100) / 100  # Truncar para 2 casas decimais
            st.write(resultado)
            st.write(f'Tempo total: {minutos} minutos e {segundos_truncados} segundos')

    # Pesquisa por mês
    elif tipo_pesquisa == 'Mês':
        mes = st.text_input('Digite o mês (MM/AAAA):')
        #mes = "12/2022"  # Exemplo de formato mes/ano
        
        if st.button('Pesquisar'):
            #resultado = df[df['Data'].str.startswith(mes)]
            resultado = df[df['Data'].str.slice(3,10) == str(mes)]
            
            total_segundos = resultado['Tempo_audio'].sum()
            minutos, segundos = divmod(total_segundos, 60)
            segundos_truncados = math.floor(segundos * 100) / 100  # Truncar para 2 casas decimais
            st.write(resultado)
            st.write(f'Tempo total: {minutos} minutos e {segundos_truncados} segundos')

    # Pesquisa por palavra-chave no tema
    elif tipo_pesquisa == 'Palavra-chave no Tema':
        palavra_chave = st.text_input('Digite a palavra-chave:')
        if st.button('Pesquisar'):
            resultado = df[df['Tema'].str.contains(palavra_chave, case=False)]
            total_segundos = resultado['Tempo_audio'].sum()
            minutos, segundos = divmod(total_segundos, 60)
            segundos_truncados = math.floor(segundos * 100) / 100  # Truncar para 2 casas decimais
            st.write(resultado)
            st.write(f'Tempo total: {minutos} minutos e {segundos_truncados} segundos')

 # Página de Ajuda
elif opcao == 'Ajuda':
    st.title('Ajuda')
    st.write('Este script foi feito com base nos 365 podcasts diários no Telegram e Spotify, desde 08/11/2022, até 07/11/2023.')
    st.write('Cada podcast tem conteúdos sobre a área de Ciência de Dados, mostrando as experiências do Professor Eduardo Rocha, que fez a gravação de todos os 365 áudios, mais 2 podcasts extras "Over Delivery".')
    st.write('É um índice dos podcasts do Telegram e também migrados para o Spotify, tem a opção de pesquisa por: número do podcast, por mês ou por palavra-chave.')
    st.write('Na época, a ideia era fazer a transcrição do áudio em texto, mas para isto, exigia um grande espaço em disco e processamento demorado. Portanto, não tem esta transcrição, por enquanto.')

# Página para listar todos os podcasts
elif opcao == 'Listar todos os podcasts':
    listar_todos_podcasts()
