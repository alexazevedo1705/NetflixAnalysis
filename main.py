import matplotlib.pyplot as plt
import pandas as pd
df = pd.read_csv('ViewingActivity.csv')

#Analisando o tamanho do arquivo
shape = df.shape
print(shape)

#Preview dos dados
#head = df.head(5)
#print(head)

#Excluindo colunas desnecessárias
df = df.drop(['Country', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark'], axis=1)
#teste de exclusão
#head = df.head(5)
#print(head)

#verificando tipos de arquivos
#tipo = df.dtypes
#print(tipo)

#transformar tempo de inicio em um formato que o pandas consegue usar em cálculos
df['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
df = df.set_index('Start Time')
df.index = df.index.tz_convert('America/Fortaleza')
df = df.reset_index()

#converter duration para timedelta
df['Duration'] = pd.to_timedelta(df['Duration'])

#teste de conversões
#tipo = df.dtypes
#print(tipo)

#filtrando reproduções menores que 2 minutos
df = df[(df['Duration'] > '0 days 00:02:00')]

#teste pra ver se o filtro funcionou
#shape = df.shape
#print(shape)
#print(df.head(5))

#Soma total de tempo assistido
#soma = df['Duration'].sum()
#print(soma)

#criar um novo dataframe com os dados somente do perfil Alex
alex = df[df['Profile Name'].str.contains('Alex', regex=False)]
deborah = df[df['Profile Name'].str.contains('Deborah', regex=False)]
tonia = df[df['Profile Name'].str.contains('Tônia', regex=False)]
manuela = df[df['Profile Name'].str.contains('Manuela', regex=False)]
#print(alex.shape)

#Soma do tempo que eu passei assistindo no app
somaalex = alex['Duration'].sum()
somadeborah = deborah['Duration'].sum()
somatonia = tonia['Duration'].sum()
somamanuela = manuela['Duration'].sum()
print('Total de tempo assistido por Alex = ', somaalex)
print('Total de tempo assistido por Deborah = ', somadeborah)
print('Total de tempo assistido por Tônia = ', somatonia)
print('Total de tempo assistido por Manuela = ', somamanuela)

#dia da semana e hora do dia que mais assisto
alex['Dia da Semana'] = alex['Start Time'].dt.weekday
alex['Hora'] = alex['Start Time'].dt.hour

#teste das colunas dia da semana e hora
#print(alex.head(1))

alex['Dia da Semana'] = pd.Categorical(alex['Dia da Semana'], categories=[0,1,2,3,4,5,6], ordered=True)
alex_pordia = alex['Dia da Semana'].value_counts()
alex_pordia = alex_pordia.sort_index()
alex_pordia.plot(kind='bar', figsize=(20,10), title='Reproduções por dia')

alex['Hora'] = pd.Categorical(alex['Hora'], categories=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23], ordered=True)
alex_pordia = alex['Hora'].value_counts()
alex_pordia = alex_pordia.sort_index()
alex_pordia.plot(kind='bar', figsize=(20,10), title='Reproduções por Hora')

#qual serie ou filme que passei mais tempo vendo
#alex2 = alex.groupby(by=['Title']).sum()
#print(alex2)