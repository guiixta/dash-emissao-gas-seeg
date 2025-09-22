import pandas as pd;
import plotly.express as px;
import dash 
from dash import html, dcc, Input, Output, callback;
import plotly.io as pio;

pio.templates.default = "simple_white";


df = pd.read_csv('db/br_seegEmissoes.csv');

linksExternos = ['https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4']

app = dash.Dash(__name__, external_scripts=linksExternos);


setores = [];
for setor in df['nivel_1'].unique():
    setores.append(setor);


app.layout = html.Div(children=[

    html.Div(children=[
        html.H1('Dashboard Emissão de gases de efeito estufa no Brasil', className='text-xl'),
        html.H2('Dados obitidos do Sistema de Estimativas de Emissões e Remoções de Gases de Efito Estufa', className='text-sm')
    ], className='Headers flex flex-col justify-center items-center text-center'),

    html.Hr(),
        html.Div(children=[

            html.Div(children=[
                html.H1('Setor'),
                dcc.Dropdown(
                    options=setores,
                    id='filtro-setores',
                    clearable=False,
                    placeholder='Selecione um setor...',
                    searchable=False,
                    value=setores[0]
                )
            ]),

            html.Div(children=[
                html.H1('Processo emissor'),
                dcc.Dropdown(
                    value='',  
                    id='filtro-processoEmissor',
                    clearable=False,
                    placeholder='Selecione um processo..',
                    searchable=False
                )
            ]),

            html.Div(children=[
                html.H1('Forma de Emissão'),
                dcc.Dropdown(
                    value='',
                    id='filtro-formaEmissao',
                    clearable=False,
                    placeholder='Selecione um forma...',
                    searchable=False
                )
            ]),

            html.Div(children=[
                html.H1('Processo Especifico'),
                dcc.Dropdown(
                    value='',   
                    id='filtro-processoEspecifico',
                    clearable=False,
                    placeholder='Selecione um processo...',
                    searchable=False
                )
            ]),

            html.Div(children=[
                html.H1('Tipo de Atividade'),
                dcc.Dropdown(
                    value='',
                    id='filtro-tipoAtividade',
                    clearable=False,
                    placeholder='Selecione um tipo...',
                    searchable=False
                )
            ]),

            html.Div(children=[
                html.H1('Atividade Especifica'),
                dcc.Dropdown(
                    value='',
                    id='filtro-atividadeEspecifica',
                    clearable=False,
                    placeholder='Selecione uma Atividade...',
                    searchable=False
                )
            ]),
    
            html.Div(children=[
                html.H1('Tipo de Emissão'),
                dcc.Dropdown(
                    value='',
                    id='filtro-tipoEmissao',
                    clearable=False,
                    placeholder='Selecione um Tipo...',
                    searchable=False
                )
            ]),

            html.Div(children=[
                html.H1('Atividade Economica'),
                dcc.Dropdown(
                    value='',
                    id='filtro-atividadeEconomica',
                    clearable=False,
                    placeholder='Selecione uma Atividade...',
                    searchable=False
                )
            ]),

            html.Div(children=[
                html.H1('Produto'),
                dcc.Dropdown(
                    value='',
                    id='filtro-produto',
                    clearable=False,
                    placeholder='Selecione um Produto...',
                    searchable=False
                )
            ])

        ], className='Filtros w-full grid grid-cols-2 gap-2 p-3'),
    html.Hr(),

    html.Div(children=[
        
        html.Div(children=[
            dcc.Graph(
                id='grafico-Barras'
            ) 
        ], className='grafico w-[49%]'),

        html.Div(children=[
            html.H1('Gases'),
            dcc.Dropdown(
                id='filtro-gases',
                clearable=False,
                value='Todos',
                searchable=False
            ),
            html.Div(children=[
                html.H1(id='currentGas', className='border border-blue-500 rounded-full p-5 font-bold text-3xl')
            ], className='flex justify-center items-center')

        ], className='flex flex-col w-[39%] gap-2 h-auto border-1 border-black text-center p-2')
        


    ], className='Graficos flex gap-2 p-3')



], className='font-[Arial]');

@callback(
    Output('filtro-processoEmissor', 'options'),
    Output('filtro-formaEmissao', 'options'),
    Output('filtro-processoEspecifico', 'options'),
    Output('filtro-tipoAtividade', 'options'),
    Output('filtro-atividadeEspecifica', 'options'),
    Output('filtro-tipoEmissao', 'options'),
    Output('filtro-atividadeEconomica', 'options'),
    Output('filtro-produto', 'options'),
    Output('filtro-gases', 'options'),
    Output('grafico-Barras', 'figure'),
    [
        Input('filtro-setores', 'value'),
        Input('filtro-processoEmissor', 'value'),
        Input('filtro-formaEmissao', 'value'),
        Input('filtro-processoEspecifico', 'value'),
        Input('filtro-tipoAtividade', 'value'),
        Input('filtro-atividadeEspecifica', 'value'),
        Input('filtro-tipoEmissao', 'value'),
        Input('filtro-atividadeEconomica', 'value'),
        Input('filtro-produto', 'value'),
        Input('filtro-gases', 'value')
    ]
)
def atualizarNiveis(setor, processoEm, formaEm, processoEs, tipoAtv, atividadeEs, tipoEm, atividadeEc, produto, gas):

    if not setor:
        return [], [], [], [], [], [], [], [], ['Todos'], {} ;


    dffilter = df[df['nivel_1'] == setor].copy();

    if setor:
        dffilter = dffilter[dffilter['nivel_1'] == setor];
    nivel2 = dffilter['nivel_2'].unique() if setor else [];

    if processoEm:
        dffilter = dffilter[dffilter['nivel_2'] == processoEm];
    nivel3 = dffilter['nivel_3'].unique() if processoEm else [];

    if formaEm:
        dffilter = dffilter[dffilter['nivel_3'] == formaEm];
    nivel4 = dffilter['nivel_4'].unique() if formaEm else [];

    if processoEs:
        dffilter = dffilter[dffilter['nivel_4'] == processoEs];
    nivel5 = dffilter['nivel_5'].unique() if processoEs else [];

    if tipoAtv:
        dffilter = dffilter[dffilter['nivel_5'] == tipoAtv];
    nivel6 = dffilter['nivel_6'].unique() if tipoAtv else [];

    if atividadeEs:
        dffilter = dffilter[dffilter['nivel_6'] == atividadeEs];
    nivel7 = dffilter['tipo_emissao'].unique() if atividadeEs else [];

    if tipoEm:
        dffilter = dffilter[dffilter['tipo_emissao'] == tipoEm];
    nivel8 = dffilter['atividade_economica'].unique() if tipoEm else [];

    if atividadeEc:
        dffilter = dffilter[dffilter['atividade_economica'] == atividadeEc];
    nivel9 = dffilter['produto'].unique() if atividadeEc else [];

    if produto:
        dffilter = dffilter[dffilter['produto'] == produto];


    gases = ['Todos'];
    for g in dffilter['gas'].unique():
        gases.append(g)

    if gas != "Todos" and gas is not None:
        dffilter = dffilter[dffilter['gas'] == gas];


    emissaoAno = dffilter.groupby('ano', as_index=False)['emissao'].sum()

    mensagem = "Todos os gases" if gas == "Todos" or gas is None else gas;
    grfBarras = px.bar(
        emissaoAno,
        x='ano',
        y='emissao',
        title=f"Emissao de {mensagem} por {setor} ao longo dos anos",
        labels={
            'emissao': 'Emissao (Toneladas)',
            'ano': 'Anos (1970-2019)'
        },
        width=500,
        height=500

    );
   

    return nivel2, nivel3, nivel4, nivel5, nivel6, nivel7, nivel8, nivel9, gases, grfBarras

@callback(
    Output('currentGas', 'children'),
    Input('filtro-gases', 'value')
)
def mostrarGas(gas):
    if gas is not None:
        return gas;

    return 'NaN';

    
if __name__ == '__main__':
    app.run(debug=True);


