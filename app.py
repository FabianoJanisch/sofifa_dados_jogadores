import streamlit as st
import pandas as pd
import plotly.figure_factory as ff
import plotly.express as px

#Base de dados
data_copa = pd.read_csv('data/players_20.csv')

#Titulo
st.title('Copa do mundo 2020')

#Menu
with st.sidebar:
    menu = st.selectbox('Menu', options = ['Seleções', 'Gráficos'])


#Menu Seleções
if menu == 'Seleções':
    #Selecionar o país
    select = data_copa['nationality'].sort_values().unique()
    escolha = st.selectbox('Escolha o país', select)

    #Filtrar escolha dos países
    selected_country = data_copa[data_copa['nationality'] == escolha]
    selected_country.rename(columns = {'short_name': 'Nome', 'age': 'Idade', 'value_eur': 'Valores em euro'}, inplace= True)
    filtred_country = selected_country[['Nome', 'Idade', 'Valores em euro']].reset_index(drop = True)


    #Tabela filtrada
    st.table(filtred_country)



#Menu gráficos
#Selecionar o país
select = data_copa['nationality'].sort_values().unique()


if menu == 'Gráficos':
    col1, col2 = st.columns(2)
    with col1:
        filtros = st.multiselect('Filtrar por país', options=select)
    with col2:
        number_team = st.slider(label = 'Selecione a quantidade de times', min_value = 5, max_value= 15)
    if filtros:
        data_copa = data_copa[data_copa['nationality'].isin(filtros)]
    
    team_more_players = pd.DataFrame(data_copa['club'].value_counts(ascending=False)).reset_index(names='Times').head(number_team)
    team_more_players.rename(columns = {'club': 'Quantidade'}, inplace= True)

    fig1 = ff.create_table(team_more_players)
    fig2 = px.bar(team_more_players, x = 'Times', y = 'Quantidade', 
    title = f'Top {number_team} times com mais jogadores ',
    text = 'Quantidade', template='simple_white')
    

    st.plotly_chart(fig2)
    st.plotly_chart(fig1)

