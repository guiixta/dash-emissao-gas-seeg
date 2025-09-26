from functools import lru_cache
import pandas as pd;
import plotly.express as px;
import dash 
from dash import html, dcc, Input, Output, callback;
import plotly.io as pio;
import plotly.graph_objects as go;


pio.templates.default = "simple_white";

@lru_cache(maxsize=None)
def load_data():

    df = pd.read_csv('https://raw.githubusercontent.com/guiixta/dash-emissao-gas-seeg/refs/heads/main/db/br_seegEmissoes.csv');
    return df

df = load_data();

linksExternos = ['https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4']

app = dash.Dash(__name__, external_scripts=linksExternos, title="Dahsboard Emissões de Gases - SEEG");

server = app.server

setores = [];
for setor in df['nivel_1'].unique():
    setores.append(setor);


listaAnos = [];
for a in df['ano'].unique():
    listaAnos.append(a)

anos = sorted(listaAnos);

min_ano, max_ano = anos[0], anos[-1];

marks = {int(y): str(y) for y in anos if y % 5 == 0}

gases = ['Todos'];
for gas in df['gas'].unique():
    gases.append(gas);

app.layout = html.Div(children=[

    html.Div(children=[
        html.H1('Dashboard Emissão de gases de efeito estufa no Brasil', className='text-xl font-bold'),
        html.H2('Dados obitidos do Sistema de Estimativas de Emissões e Remoções de Gases de Efeito Estufa', className='text-sm')
    ], className='Headers flex flex-col justify-center items-center text-center p-3'),

    html.Hr(),
        html.Div(children=[
            
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
                    html.H1('Processo Emissor'),
                    dcc.Dropdown(
                        value='',  
                        id='filtro-processoEmissor',
                        placeholder='Selecione um processo..',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Forma de Emissão'),
                    dcc.Dropdown(
                        value='',
                        id='filtro-formaEmissao',
                        placeholder='Selecione um forma...',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Processo Especifico'),
                    dcc.Dropdown(
                        value='',   
                        id='filtro-processoEspecifico',
                        placeholder='Selecione um processo...',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Tipo de Atividade'),
                    dcc.Dropdown(
                        value='',
                        id='filtro-tipoAtividade',
                        placeholder='Selecione um tipo...',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Atividade Especifica'),
                    dcc.Dropdown(
                        value='',
                        id='filtro-atividadeEspecifica',
                        placeholder='Selecione uma Atividade...',
                        searchable=False
                    )
                ]),
        
                html.Div(children=[
                    html.H1('Tipo de Emissão'),
                    dcc.Dropdown(
                        value='',
                        id='filtro-tipoEmissao',
                        placeholder='Selecione um Tipo...',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Atividade Economica'),
                    dcc.Dropdown(
                        value='',
                        id='filtro-atividadeEconomica',
                        placeholder='Selecione uma Atividade...',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Produto'),
                    dcc.Dropdown(
                        value='',
                        id='filtro-produto',
                        placeholder='Selecione um Produto...',
                        searchable=False
                    )
                ]),

                html.Div(children=[
                    html.H1('Gás'),
                    dcc.Dropdown(
                        id='filtro-gases',
                        value='Todos',
                        clearable=False,
                        searchable=False
                    )
                ])

            ], className="rounded-lg shadow bg-white grid grid-cols-2 gap-2 p-3")



        ], className='Filtros w-full p-3 mt-3 mb-3'),
    html.Hr(),

    html.Div(children=[

        html.Div(children=[
       

            html.Div(children=[
                dcc.Graph(
                    id='grafico-Barras',
                    className='grafico-animado-barras'
                ) 
            ], className='grafico w-full p-2 bg-white rounded-lg shadow')
            

        ], className='flex flex-col'),
        
        html.Div(children=[
           
            html.Div(children=[
                html.Div(children=[
                    html.H1('Gás', className='m-0'),
                    html.P(id='currentGas', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center items-center text-center'),

                html.Div(children=[
                    html.H1(id='Ano-menor', className='m-0'),
                    html.P(id='EmissaoMenor', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center items-center text-center'),

                html.Div(children=[
                    html.H1(id='Ano-maior', className='m-0'),
                    html.P(id='EmissaoMaior', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center items-center text-center'),

                html.Div(children=[
                    html.H1(id='AnoComMaior', className='m-0'),
                    html.P(id='EmissaoDoAnoMaior', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center items-center text-center'),

                html.Div(children=[
                    html.H1(id='AnoComMenor', className='m-0'),
                    html.P(id='EmissaoDoAnoMenor', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center items-center text-center'),

                html.Div(children=[
                    html.H1(id='TotalIntervalo', className='m-0'),
                    html.P(id='SomaTotalIntervalo', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center ittems-center text-center'),

                html.Div(children=[
                    html.H1('Emissão Total', className='m-0'),
                    html.P(id='emissaoTotal', className='font-bold text-sm')
                ], className='border-1 border-black p-3 rounded-md flex flex-col justify-center ittems-center text-center')

            ], className='Cards w-full p-2 flex flex-col lg:flex-row gap-4 w-full p-2 bg-white rounded-lg shadow'),



            html.Div(children=[

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

                ])

            ], className='w-full p-2 bg-white rounded-lg shadow')
            
           
        ], className='flex flex-col gap-4 mt-4'),

        html.Div(children=[

                dcc.Loading(
                    id='loading-pizza',
                    type='default',
                    className="w-full lg:w-1/2",
                    children=[
                        dcc.Graph(
                            id='grafico-pizza',
                            className="rounded-lg bg-white p-1"
                        )
                    ]),

                html.Div(children=[
                    html.H1('Gases', className='text-white font-bold'),
                    dcc.Dropdown(
                        options=gases,
                        id="filtro-gases2",
                        value='Todos',
                        clearable=False,
                        className="mb-2"
                    ),
                    dcc.Loading(children=[
                        dcc.Graph(
                            id='grafico-pizzaSetor',
                            className="rounded-lg bg-white p-1"
                        )
                    ], id="Loading-pizzaSetor", type="default")
                ], className="p-3 bg-stone-500 flex flex-col flex-grow w-full lg:w-1/2 rounded-lg shadow")

            ], className='flex flex-col lg:flex-row mt-3 bg-white rounded-lg shadow')


    ], className='Graficos flex p-3 flex-col pb-30'),

    html.Footer(children=[
        html.Div(children=[
            html.P("Fontes:", className="mr-4 font-semibold cursor-default"),
            html.A(
                href="https://basedosdados.org/dataset/9a22474f-a763-4431-8e3d-667908a1c7ab?table=104c6201-b0e7-47aa-b858-83252e2b149f",
                target="_blank",
                children=[
                    html.Img(src=app.get_asset_url('baseDosDados.png'), className="h-10 hover:opacity-75 transition-opacity")
                ]),
            html.A(
                href="https://seeg.eco.br/",
                target="_blank",
                children=[
                    html.Img(src=app.get_asset_url('seegLogo.png'), className="h-10 ml-4 hover:opacity-75 transition-opacity")
            ])
        ], className="flex items-center p-2"),
    
        html.Span(className="p-[0.5px] bg-black w-full flex"),

        html.P(children=[
            'Feito por: ',
            html.A('Guiixta', href="https://github.com/guiixta", target="_blank", className="font-bold text-black hover:underline")
        ])
    ], className="flex flex-col w-dvw z-50 absolute border-t-1 border-black left-0 bottom-0 p-1 justify-center text-center items-center bg-white")

], className='font-[Montserrat] relative min-h-dvh bg-[#fc973f]');

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

    linhaCresimentoPositiva = linhaCresimento[linhaCresimento['emissao'] > 0];

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
        linhaCresimentoPositiva,
        x='ano',
        y='emissao',
        title=f'Crescimento da emissão',
        labels={'ano': f'Anos ({intervalo[0]} - {intervalo[1]})', 'emissao': 'Emissao (Toneladas)'},
        markers=True
    );


    emissaoAno = dffilter.groupby('ano', as_index=False)['emissao'].sum();

    emissaoAnoPositiva = emissaoAno[emissaoAno['emissao'] > 0]

    emissaoTotal = f"{dffilter['emissao'].sum():.2f} (t)"

    mensagem = "Todos os gases" if gas == "Todos" or gas is None else gas;
    grfBarras = px.bar(
        emissaoAnoPositiva,
        x='ano',
        y='emissao',
        title=f"Emissão de {mensagem} por {setor} ao longo dos anos",
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


@callback(
    Output('grafico-pizza', 'figure'),
    [
        Input('filtro-setores', 'value'),
        Input('filtro-gases', 'value')
    ]
)
def porcentagemDeEmissaoDosProcessos(setor, gas):
    
    if gas == "Todos":

        dffilter = df[df['nivel_1'] == setor].copy();

        porcentagem = dffilter.groupby('nivel_2', as_index=False)['emissao'].sum();

        porcentagem_positiva = porcentagem[porcentagem['emissao'] > 0];

        # Se, após filtrar, não sobrar nenhum dado, retorna um gráfico vazio e amigável.
        if porcentagem_positiva is None:
            fig = go.Figure()
            fig.update_layout(title=f'Não há fontes de emissão para {setor}')
            return fig

        grfPizza = px.pie(
            porcentagem_positiva,
            values='emissao',
            names='nivel_2',
            title=f"Porcentagem de emissão de Todos os gases por processos de {setor}",
            labels={'nivel_2': 'Processo'}
        )

        grfPizza.update_layout(title=dict(font=dict(size=13)))
        
        
        return grfPizza

    dffilterGas = df[df['nivel_1'] == setor].copy();

    filtroGas = dffilterGas[dffilterGas['gas'] == gas];

    processoGas = filtroGas.groupby('nivel_2', as_index=False)['emissao'].sum();

    processoPositivo = processoGas[processoGas['emissao'] > 0];

    if processoPositivo is None:
        fig = go.Figure()
        fig.update_layout(title=f'Não há valores de emissao para {gas}')
        return fig


    grfPizzaGas = px.pie(
        processoPositivo,
        values='emissao',
        names='nivel_2',
        title=f"Porcetagem de emissão de {gas} por processo de {setor}",
        labels={
            'nivel_2': 'Processo'
        }
    )

    grfPizzaGas.update_layout(title=dict(font=dict(size=13)))


    return grfPizzaGas


@callback(
    Output('grafico-pizzaSetor', 'figure'),
    [
        Input('filtro-gases2', 'value')
    ]
)
def emissãoSetor(gas):
    if gas == "Todos":
        emissaoSetores = df.groupby('nivel_1', as_index=False)['emissao'].sum();

        emissaoPositiva = emissaoSetores[emissaoSetores['emissao'] > 0];

        grfPizzaSetor = px.pie(
            emissaoPositiva,
            values='emissao',
            names='nivel_1',
            title=f"Porcetagem de emissão de Todos os gases por setores",
            labels={'nivel_1': 'Setor'}

        )

        grfPizzaSetor.update_layout(title=dict(font=dict(size=13)))

        return grfPizzaSetor


    dffilter = df[df['gas'] == gas];

    emissaoSetores = dffilter.groupby('nivel_1', as_index=False)['emissao'].sum();

    emissaoPositiva = emissaoSetores[emissaoSetores['emissao'] > 0];

    grfPizzaSetor = px.pie(
            emissaoPositiva,
            values='emissao',
            names='nivel_1',
            title=f"Porcetagem de emissão de {gas} por setores",
            labels={'nivel_1': 'Setor'}

        )

    grfPizzaSetor.update_layout(title=dict(font=dict(size=13)))

    return grfPizzaSetor
 




    
if __name__ == '__main__':
    app.run(debug=True);


