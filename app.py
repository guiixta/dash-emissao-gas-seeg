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


listaAnos = [];
for a in df['ano'].unique():
    listaAnos.append(a)

anos = sorted(listaAnos);

min_ano, max_ano = anos[0], anos[-1];

marks = {int(y): str(y) for y in anos if y % 5 == 0}

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
            ]),

            html.Div(children=[
                html.H1('Gás'),
                dcc.Dropdown(
                    id='filtro-gases',
                    clearable=False,
                    value='Todos',
                    searchable=False
                )
            ])

        ], className='Filtros w-full grid grid-cols-2 gap-2 p-3'),
    html.Hr(),

    html.Div(children=[

        html.Div(children=[
       

            html.Div(children=[
                dcc.Graph(
                    id='grafico-Barras'
                ) 
            ], className='grafico w-full p-2 bg-white rounded-lg shadow')


        ], className='flex flex-col'),
        
        html.Div(children=[
           
            html.Div(children=[
                html.Div(children=[
                    html.H1('Gás'),
                    html.P(id='currentGas', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md'),

                html.Div(children=[
                    html.H1(id='Ano-menor'),
                    html.P(id='EmissaoMenor', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md'),

                html.Div(children=[
                    html.H1(id='Ano-maior'),
                    html.P(id='EmissaoMaior', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md'),

                html.Div(children=[
                    html.H1(id='AnoComMaior'),
                    html.P(id='EmissaoDoAnoMaior', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md'),

                html.Div(children=[
                    html.H1(id='AnoComMenor'),
                    html.P(id='EmissaoDoAnoMenor', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md'),

                html.Div(children=[
                    html.H1(id='TotalIntervalo'),
                    html.P(id='SomaTotalIntervalo', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md'),

                html.Div(children=[
                    html.H1('Emissão Total'),
                    html.P(id='emissaoTotal', className='font-bold')
                ], className='border-1 border-black p-3 rounded-md')

            ], className='Cards w-full p-2 flex flex-col lg:flex-row gap-4'),



            html.Div(children=[

                dcc.Graph(
                    id='grafico-Linhas'
                ),
                
                dcc.RangeSlider(
                    min=min_ano,
                    max=max_ano,
                    marks=marks,
                    value=[min_ano, max_ano],
                    id='intervaloAnos',
                    className='p-4'
                )

            ], className='w-full p-2 bg-white rounded-lg shadow')
            
           
        ], className='flex flex-col gap-4 mt-4')


    ], className='Graficos flex p-3 flex-col')



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
    Output('grafico-Linhas', 'figure'),
    Output('Ano-menor', 'children'),
    Output('EmissaoMenor', 'children'),
    Output('Ano-maior', 'children'),
    Output('EmissaoMaior', 'children'),
    Output('emissaoTotal', 'children'),
    Output('TotalIntervalo', 'children'),
    Output('SomaTotalIntervalo', 'children'),
    Output('AnoComMaior', 'children'),
    Output('EmissaoDoAnoMaior', 'children'),
    Output('AnoComMenor', 'children'),
    Output('EmissaoDoAnoMenor', 'children'),
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
        Input('filtro-gases', 'value'),
        Input('intervaloAnos', 'value')
    ]
)
def atualizarNiveis(setor, processoEm, formaEm, processoEs, tipoAtv, atividadeEs, tipoEm, atividadeEc, produto, gas, intervalo):

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
    nivel5 = dffilter['nivel_5'].unique() if  processoEs else [];

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

    dffLinha = dffilter

    if intervalo:
        dffLinha = dffilter[(dffilter['ano'] >= intervalo[0]) & (dffilter['ano'] <= intervalo[1])];

    linhaCresimento = dffLinha.groupby('ano', as_index=False)['emissao'].sum();

    mensagemAnoMenor = f"Emissão de {intervalo[0]}";

    mensagemAnoMaior = f"Emissao de {intervalo[1]}";

    mensagemTotalIntervalo = f"Total entre: {intervalo[0]} a {intervalo[1]}";

    linhaMaiorEmissao = linhaCresimento.loc[linhaCresimento['emissao'].idxmax()];

    linhaMenorEmissao = linhaCresimento.loc[linhaCresimento['emissao'].idxmin()];

    mensagemAnoComMenor = f"Ano com menor emissão ({int(linhaMenorEmissao['ano'])})";

    mensagemAnoComMaior = f"Ano com maior emisssao ({int(linhaMaiorEmissao['ano'])})";

    valorMaiorEmissao = f'{linhaMaiorEmissao['emissao']:.2f} (t)';

    valorMenorEmissao = f'{linhaMenorEmissao['emissao']:.2f} (t)';

    anoMenor = dffLinha[dffLinha['ano'] == intervalo[0]];

    anoMaior = dffLinha[dffLinha['ano'] == intervalo[1]];

    quantidadeEmissaoAnoMenor = f'{anoMenor['emissao'].sum():.2f} (t)';

    quantidadeEmissaoAnoMaior = f'{anoMaior['emissao'].sum():.2f} (t)';

    emissaoIntervalo = linhaCresimento[(linhaCresimento['ano'] >= intervalo[0]) & (linhaCresimento['ano'] <= intervalo[1])];

    somaTotalIntervalo = f'{emissaoIntervalo['emissao'].sum():.2f} (t)'

    grfLinha = px.line(
        linhaCresimento,
        x='ano',
        y='emissao',
        title=f'Crescimento da emissão',
        labels={'ano': f'Anos ({intervalo[0]} - {intervalo[1]})', 'emissao': 'Emissao (Toneladas)'},
        markers=True
    );


    emissaoAno = dffilter.groupby('ano', as_index=False)['emissao'].sum();

    emissaoTotal = f"{dffilter['emissao'].sum():.2f} (t)"

    mensagem = "Todos os gases" if gas == "Todos" or gas is None else gas;
    grfBarras = px.bar(
        emissaoAno,
        x='ano',
        y='emissao',
        title=f"Emissao de {mensagem} por {setor} ao longo dos anos",
        labels={
            'emissao': 'Emissao (Toneladas)',
            'ano': 'Anos (1970 - 2019)'
        }
       
    );

    grfBarras.update_layout(
        title=dict(font=dict(size=15))
    );
   

    return nivel2, nivel3, nivel4, nivel5, nivel6, nivel7, nivel8, nivel9, gases, grfBarras, grfLinha, mensagemAnoMenor, quantidadeEmissaoAnoMenor, mensagemAnoMaior, quantidadeEmissaoAnoMaior, emissaoTotal, mensagemTotalIntervalo, somaTotalIntervalo, mensagemAnoComMaior, valorMaiorEmissao, mensagemAnoComMenor, valorMenorEmissao

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


